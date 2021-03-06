from typing import Any, NamedTuple

import ujson
from bs4 import BeautifulSoup


class RequestBody(NamedTuple):
    url: str
    method: str = "GET"
    headers: Any = None
    params: Any = None
    data: Any = None
    proxy: Any = None
    meta: Any = None
    callback: Any = None


class Response:
    __slots__ = ("url", "method", "headers", "status", "meta", "text", "callback")

    def __init__(self, url, method, headers, text, status, meta, callback) -> None:
        self.url = url
        self.method = method
        self.text = text
        self.status = status
        self.meta = meta
        self.headers = headers
        self.callback = callback

    def json(self):
        return ujson.loads(self.text)

    def follow(
        self,
        url,
        meta=None,
        method=None,
        headers=None,
        callback=None,
    ):
        method = method or self.method
        headers = headers or self.headers
        callback = callback or self.callback
        return RequestBody(
            url, method=method, headers=headers, callback=callback, meta=meta
        )

    def html_tree(self):
        """
        Return etree HTML
        """
        bs = BeautifulSoup(self.text, "lxml")
        return bs
