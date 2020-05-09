import os.path
import filehandler

ORDER_FILE = 'order.txt'
RELEASE_NOTES_FILE = 'release_notes.txt'

if os.path.isfile(ORDER_FILE):
    _cache = filehandler.read_as_json(ORDER_FILE)
else:
    _cache = {}


def update_item(item, comment, is_checked) -> None:
    _cache[item] = {'comment': comment, 'is_checked': is_checked}
    filehandler.write_as_json(ORDER_FILE, _cache)


def get_item(item) -> dict:
    return {item: _cache[item]}


def remove_item(item) -> None:
    del _cache[item]
    filehandler.write_as_json(ORDER_FILE, _cache)


def get_order() -> dict:
    return _cache


def remove_order() -> None:
    _cache.clear()
    filehandler.write_as_json(ORDER_FILE, _cache)


def get_release_notes() -> str:
    data = filehandler.read_plain(RELEASE_NOTES_FILE)
    return data;
