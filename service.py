import os.path
import filehandler

ORDER_TEMPLATE = 'order_{}.json'
RELEASE_NOTES_FILE = 'release_notes.txt'


def get_order_filename(order_id: int) -> str:
    return ORDER_TEMPLATE.format(order_id)


def update_item(order_id: int, item: dict) -> None:
    order_filename = get_order_filename(order_id)
    item_id = item.get('id')
    _cache[order_filename][item_id] = item
    filehandler.write_as_json(order_filename, _cache[order_filename])


def change_item_position(order_id: int, item_id: str, position: int) -> None:
    order_filename = get_order_filename(order_id)
    old_dict = _cache[order_filename].copy()
    keys = list(old_dict.keys())
    old_index = keys.index(item_id)
    keys.insert(int(position), keys.pop(old_index))
    new_dict = {}
    for key in keys:
        new_dict[key] = old_dict[key]
    _cache[order_filename] = new_dict
    filehandler.write_as_json(order_filename, _cache[order_filename])


def remove_item(order_id: int, item_id: str) -> None:
    order_filename = get_order_filename(order_id)
    del _cache[order_filename][item_id]
    filehandler.write_as_json(order_filename, _cache[order_filename])


def get_order(order_id: int) -> list:
    order_filename = get_order_filename(order_id)
    return list(_cache[order_filename].values())


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
        orders_lengths.append(len(order.values()))
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
