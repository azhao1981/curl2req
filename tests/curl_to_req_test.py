# -*- coding: utf-8 -*-
from curl2req import curl_to_req, get_json_paths


def test_curl_to_req():
    curl_to_req(
        "tests/test.curl",
        xpath="",
        dir_name=".res",
        output_file_prefix="temp",
    )


def test_get_json_paths():
    json_content = '{"a": {"b": 1, "c": [2, 3, [{"d": 4}]]}}'
    get_json_paths(json_content, uniq_path=True)


if __name__ == "__main__":
    test_curl_to_req()
    test_get_json_paths()
