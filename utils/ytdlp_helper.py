import os
import sys

import yt_dlp

FFMPEG_OPTIONS = {
    "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
    "options": "-vn",
}

BASE_OPTIONS = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",
}

_BROWSER_PATHS = {
    "darwin": {
        "chrome":   "~/Library/Application Support/Google/Chrome",
        "edge":     "~/Library/Application Support/Microsoft Edge",
        "brave":    "~/Library/Application Support/BraveSoftware/Brave-Browser",
        "chromium": "~/Library/Application Support/Chromium",
        "firefox":  "~/Library/Application Support/Firefox",
        "safari":   "~/Library/Safari",
    },
    "linux": {
        "chrome":   "~/.config/google-chrome",
        "chromium": "~/.config/chromium",
        "edge":     "~/.config/microsoft-edge",
        "brave":    "~/.config/BraveSoftware/Brave-Browser",
        "firefox":  "~/.mozilla/firefox",
    },
    "win32": {
        "chrome":   os.path.expandvars(r"%LOCALAPPDATA%\Google\Chrome\User Data"),
        "edge":     os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\User Data"),
        "brave":    os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data"),
        "firefox":  os.path.expandvars(r"%APPDATA%\Mozilla\Firefox"),
    },
}


def _detect_browser():
    platform = "linux" if sys.platform.startswith("linux") else sys.platform
    paths = _BROWSER_PATHS.get(platform, {})
    for browser, path in paths.items():
        if os.path.exists(os.path.expanduser(path)):
            return browser
    return None


_browser = _detect_browser()
print(f"browser for cookies: {_browser or 'none found'}")


def get_ytdl(with_cookies: bool = True):
    opts = dict(BASE_OPTIONS)
    if with_cookies and _browser:
        opts["cookiesfrombrowser"] = (_browser,)
    return yt_dlp.YoutubeDL(opts)
