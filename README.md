# simple_status

[![NoSkid Verification](https://noskid.today/badge/470x200/?repo=Toasterclan1/simple_status)](https://noskid.today)

`simple_status` is a lean Python library for setting Discord Rich Presence with minimal boilerplate. It’s ideal for personal tools, games, and development utilities where you want a quick presence update.

## features

- Set rich activity details with a single API call
- Support for `title`, `state`, `details`, and time
- Large and small image keys, plus clickable button action
- Optional `client_id` (defaults to a built-in app ID for convenience)
- Minimal dependency scope and easy script integration

## Installation

Install from PyPI:

```bash
pip install simple_status
```

## Quick start

```python
import time
import simple_status

simple_status.set(
    client_id="YOUR_DISCORD_APP_ID",        # Optional; uses default app ID if blank
    title="My Cool App",
    state="Working on automation",
    details="Generating random content",
    large_image="logo",                  # Discord asset key from app dashboard (requires client_id)
    small_image="small_logo",            # Optional second image asset key (require client_id)
    button=("Visit docs", "https://example.com")
)

# Keep process alive, presence updates are pushed automatically
while True:
    time.sleep(15)
```



## Discord setup

1. Open Discord Developer Portal
2. Create an application
3. Upload image assets (keys used in `large_image`/`small_image`)
4. Copy the application ID to `client_id`

##  Notes

- Discord Rich Presence requires the Discord client running locally.
- Changes may take a few seconds to appear.
- To use images you need to use your own app id

## FAQ

1. *Why isn't my image working?*:
To use images make sure you are using your own app id, set with client_id, then make sure the image is uploaded to discord devolper portal
*Any further questions DM me on discord (Toaster_clan_1)*

## License

This project is licensed under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/).

- Permission granted to copy, share, and adapt.
- Must provide attribution to the original author.
- Commercial use (selling or selling copies) is prohibited.

