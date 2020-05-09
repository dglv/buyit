import codecs
import json


def write_plain(filename: str, text: str) -> None:
    with codecs.open(filename, 'w', encoding='utf-8') as fd:
        print(text, file=fd)


def read_plain(filename: str) -> str:
    with codecs.open(filename, 'r', encoding='utf-8') as fd:
        return fd.read()


def write_as_json(filename: str, data: dict) -> None:
    with codecs.open(filename, 'w', encoding='utf-8') as fd:
        print(json.dumps(data, ensure_ascii=False), file=fd)


def read_as_json(filename: str) -> dict:
    with codecs.open(filename, 'r', encoding='utf-8') as fd:
        json_output = {}
        data = fd.read()
        if data:
            json_output = json.loads(data)
        return json_output
