#!/bin/sh
# Builds index.html (installable home screen app) from app.html (the claude.ai artifact page).
cd "$(dirname "$0")"
{
  printf '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
  printf '<link rel="manifest" href="manifest.webmanifest"><meta name="theme-color" content="#ff6b4a">\n'
  printf '<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png"><link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
  printf '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">\n'
  printf '<meta name="apple-mobile-web-app-status-bar-style" content="default"><meta name="apple-mobile-web-app-title" content="SpeakUp">\n'
  printf '<style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}</style>\n'
  printf '</head><body>\n'
  cat app.html
  printf '\n<script>if("serviceWorker" in navigator&&(location.protocol==="https:"||location.hostname==="localhost")){navigator.serviceWorker.register("sw.js").catch(function(){})}</script>\n'
  printf '</body></html>\n'
} > index.html
