# -*- coding: utf-8 -*-
from curl2req import curl_to_req


def test_curl_to_req():
    curl_to_req(
        "tests/test.curl",
        xpath="",
        dir_name=".res",
        output_file_prefix="temp",
    )


if __name__ == "__main__":
    test_curl_to_req()

