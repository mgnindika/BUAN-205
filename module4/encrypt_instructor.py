#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Encrypt the instructor notes into a password-gated page.

    python module4/encrypt_instructor.py                 # prompts for the password
    python module4/encrypt_instructor.py --password ...  # non-interactive

Reads  module4/instructor.source.html  (plaintext, gitignored, never published)
Writes module4/instructor.html         (encrypted, safe to publish)

The whole document is encrypted with AES-GCM under a key derived from the
password by PBKDF2-SHA256. The published file contains ciphertext and nothing
else: no answer text, no plaintext fragments. Without the password a visitor
cannot recover the notes from the page, from "view source", or from devtools.

This is real encryption, not a JavaScript show/hide gate. Its strength is the
strength of the password -- anyone you give the password to can read it, and
can pass it on.

Re-run this after every edit to instructor.source.html.
"""
import argparse
import base64
import getpass
import gzip
import hashlib
import io
import json
import os
import secrets
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "instructor.source.html"
OUT = HERE / "instructor.html"

# OWASP's 2023 floor for PBKDF2-HMAC-SHA256. Costs a browser roughly a second,
# which is fine once per class and expensive to brute-force.
ITERATIONS = 600_000


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>Instructor copy | BUAN B205</title>
<style>
  :root {{ --maroon:#7b1e3a; --ink:#1c1c1c; --paper:#fdfdfb; --wash:#f2f0ec; --slate:#5b6472; }}
  * {{ box-sizing:border-box; }}
  body {{ margin:0; min-height:100vh; display:grid; place-items:center; padding:1.5rem;
         background:var(--wash); color:var(--ink);
         font-family:"Libre Franklin",system-ui,-apple-system,sans-serif; }}
  .box {{ width:100%; max-width:26rem; background:var(--paper); border-radius:14px;
          padding:2rem 1.8rem; box-shadow:0 10px 34px rgba(0,0,0,.10); }}
  h1 {{ margin:0 0 .3rem; font-size:1.3rem; }}
  p.sub {{ margin:0 0 1.4rem; color:var(--slate); font-size:.92rem; line-height:1.5; }}
  label {{ display:block; font-size:.85rem; font-weight:600; margin-bottom:.4rem; }}
  input {{ width:100%; font-size:1rem; padding:.62rem .7rem; border:1.5px solid #cfcac2;
           border-radius:8px; background:#fff; color:var(--ink); }}
  input:focus {{ outline:none; border-color:var(--maroon); }}
  button {{ width:100%; margin-top:.9rem; font-size:.95rem; font-weight:700; cursor:pointer;
            padding:.62rem 1rem; border:0; border-radius:999px;
            background:var(--maroon); color:#fff; }}
  button:hover {{ background:#651730; }}
  button[disabled] {{ opacity:.65; cursor:progress; }}
  .msg {{ min-height:1.3em; margin-top:.8rem; font-size:.87rem; font-weight:600; color:var(--maroon); }}
  .foot {{ margin-top:1.3rem; font-size:.78rem; color:var(--slate); line-height:1.5; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --ink:#ece9e4; --paper:#242427; --wash:#18181a; --slate:#a3a9b4; --maroon:#e0879f; }}
    input {{ background:#2e2e32; border-color:#44444a; color:var(--ink); }}
    button {{ color:#241018; }}
  }}
</style>
</head>
<body>
<div class="box">
  <h1>Instructor copy</h1>
  <p class="sub">BUAN B205, Module 4. These notes include the answer keys. Students use the
     <a href="index.html">student page</a>.</p>
  <form id="f" autocomplete="off">
    <label for="pw">Password</label>
    <input id="pw" type="password" autofocus autocomplete="current-password">
    <button id="go" type="submit">Unlock</button>
  </form>
  <div class="msg" id="msg" role="status" aria-live="polite"></div>
  <p class="foot">The page is stored encrypted. The password is never sent anywhere &mdash;
     it is used in your browser to decrypt it.</p>
</div>
<script>
(function () {{
  var P = {payload};
  var f = document.getElementById('f'),
      pw = document.getElementById('pw'),
      go = document.getElementById('go'),
      msg = document.getElementById('msg'),
      KEY = 'buan205-m4-instructor';

  function b64(s) {{
    var raw = atob(s), a = new Uint8Array(raw.length);
    for (var i = 0; i < raw.length; i++) a[i] = raw.charCodeAt(i);
    return a;
  }}

  async function unlock(pass, quiet) {{
    var enc = new TextEncoder();
    var base = await crypto.subtle.importKey('raw', enc.encode(pass), 'PBKDF2', false, ['deriveKey']);
    var key = await crypto.subtle.deriveKey(
      {{ name:'PBKDF2', salt:b64(P.salt), iterations:P.iterations, hash:'SHA-256' }},
      base, {{ name:'AES-GCM', length:256 }}, false, ['decrypt']);
    var plain = await crypto.subtle.decrypt(
      {{ name:'AES-GCM', iv:b64(P.iv) }}, key, b64(P.data));   // throws on a wrong password
    var stream = new Blob([plain]).stream().pipeThrough(new DecompressionStream('gzip'));
    var html = await new Response(stream).text();
    try {{ sessionStorage.setItem(KEY, pass); }} catch (e) {{}}
    document.open(); document.write(html); document.close();
  }}

  f.addEventListener('submit', async function (e) {{
    e.preventDefault();
    if (!pw.value) return;
    go.disabled = true; msg.textContent = 'Decrypting\\u2026';
    try {{
      await unlock(pw.value);
    }} catch (err) {{
      go.disabled = false;
      msg.textContent = 'That password does not open this page.';
      pw.select();
    }}
  }});

  // Re-entering the tab (e.g. back from the notebook) should not re-prompt.
  var saved = null;
  try {{ saved = sessionStorage.getItem(KEY); }} catch (e) {{}}
  if (saved) unlock(saved).catch(function () {{
    try {{ sessionStorage.removeItem(KEY); }} catch (e) {{}}
  }});
}})();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--password", help="set it non-interactively (it lands in your shell history)")
    ap.add_argument("--source", default=str(SRC), help="plaintext instructor notes")
    ap.add_argument("--out", default=str(OUT), help="encrypted page to write")
    args = ap.parse_args()

    src = Path(args.source)
    if not src.exists():
        sys.exit(f"no plaintext at {src}\n"
                 f"Keep the readable notes there; this script encrypts them into {Path(args.out).name}.")

    plain = src.read_bytes()
    if b'class="key"' not in plain:
        print("warning: the source has no answer-key boxes -- is it the student page?", file=sys.stderr)

    password = args.password or getpass.getpass("Password for the instructor page: ")
    if not args.password:
        if password != getpass.getpass("Again: "):
            sys.exit("the two passwords differ")
    if len(password) < 8:
        sys.exit("use at least 8 characters")

    # gzip first: the notes are ~150KB of repetitive HTML and compress ~8x, which
    # keeps the published page small. The browser inflates it after decrypting.
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", mtime=0) as gz:
        gz.write(plain)
    packed = buf.getvalue()

    salt = secrets.token_bytes(16)
    iv = secrets.token_bytes(12)
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, ITERATIONS, dklen=32)

    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    except ImportError:
        sys.exit("needs the cryptography package: pip install cryptography")
    blob = AESGCM(key).encrypt(iv, packed, None)

    payload = json.dumps({
        "salt": base64.b64encode(salt).decode(),
        "iv": base64.b64encode(iv).decode(),
        "data": base64.b64encode(blob).decode(),
        "iterations": ITERATIONS,
    }, indent=None)

    out = Path(args.out)
    out.write_text(SHELL.format(payload=payload), encoding="utf-8", newline="\n")

    print(f"  source     {src.name}: {len(plain):,} bytes")
    print(f"  gzipped    {len(packed):,} bytes")
    print(f"  encrypted  {out.name}: {out.stat().st_size:,} bytes")
    print(f"  PBKDF2-SHA256 x {ITERATIONS:,}, AES-256-GCM")
    print(f"\nWrote {out}. Publish that; keep {src.name} out of git.")


if __name__ == "__main__":
    main()
