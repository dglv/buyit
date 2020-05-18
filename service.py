import os.path
import filehandler

ORDER_TEMPLATE = 'order_{}.json'
RELEASE_NOTES_FILE = 'release_notes.txt'


def get_order_filename(order_id: int) -> str:
    return ORDER_TEMPLATE.format(order_id)


def update_item(order_id: int, item: str, comment: str, is_checked: str) -> None:
    order_filename = get_order_filename(order_id)
    _cache[order_filename][item] = {'comment': comment, 'is_checked': is_checked}
    filehandler.write_as_json(order_filename, _cache[order_filename])


def change_item_position(order_id: int, item: str, position: int) -> None:
    order_filename = get_order_filename(order_id)
    old_dict = _cache[order_filename].copy()
    old_keys = []
    for key in old_dict.keys():
        old_keys.append(key)
    old_index = old_keys.index(item)
    old_keys.insert(int(position), old_keys.pop(old_index))
    new_dict = {}
    for key in old_keys:
        new_dict[key] = old_dict[key]
    _cache[order_filename] = new_dict
    filehandler.write_as_json(order_filename, _cache[order_filename])


def get_item(order_id: int, item: str) -> dict:
    order_filename = get_order_filename(order_id)
    return {item: _cache[order_filename][item]}


def remove_item(order_id: int, item: str) -> None:
    order_filename = get_order_filename(order_id)
    del _cache[order_filename][item]
    filehandler.write_as_json(order_filename, _cache[order_filename])


def get_order(order_id: int) -> dict:
    order_filename = get_order_filename(order_id)
    return _cache[order_filename]


def remove_order(order_id: int) -> None:
    order_filename = get_order_filename(order_id)
    _cache[order_filename] = {}
    filehandler.write_as_json(order_filename, _cache[order_filename])


def get_release_notes() -> str:
    data = filehandler.read_plain(RELEASE_NOTES_FILE)
    return data


def get_orders_lengths() -> list:
    orders_lengths = []
    for order in _cache.values():
        orders_lengths.append(len(order))
    return orders_lengths


_cache = {}
for i in range(8):
    _order_id = i + 1
    _order_filename = get_order_filename(_order_id)
    if os.path.isfile(_order_filename):
        _cache[_order_filename] = filehandler.read_as_json(_order_filename)
    else:
        _cache[_order_filename] = {}
        filehandler.write_as_json(_order_filename, _cache[_order_filename])
