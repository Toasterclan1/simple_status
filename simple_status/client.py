from pypresence import Presence

_rpc = None
_DEFAULT_CLIENT_ID = "1488205329069113394"

def connect(client_id: str = None):
    global _rpc
    if not client_id:
        client_id = _DEFAULT_CLIENT_ID

    _rpc = Presence(client_id)
    _rpc.connect()
    return _rpc

def set(
    title: str = "",
    state: str = "",
    details: str = "",
    large_image: str = None,
    small_image: str = None,
    button: tuple = None,
    client_id: str = None,
):
    global _rpc

    if _rpc is None:
        connect(client_id)

    buttons = None
    if button:
        label, url = button
        buttons = [{"label": label, "url": url}]

    payload = {
        "state": state,
        "details": details or title,
    }

    if large_image:
        payload["large_image"] = large_image

    if small_image:
        payload["small_image"] = small_image

    if buttons:
        payload["buttons"] = buttons

    _rpc.update(**payload)

def clear():
    global _rpc
    if _rpc is not None:
        _rpc.clear()
