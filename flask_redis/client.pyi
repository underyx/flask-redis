from typing import Union

from flask import Flask
from redis import Redis, StrictRedis


class FlaskRedis(Redis):
    def __init__(
        self,
        app: Flask = None,
        strict: bool = True,
        config_prefix: str = "REDIS",
        **kwargs
    ) -> None: ...

    @classmethod
    def from_custom_provider(
        cls,
        provider: Union[StrictRedis, Redis],
        app: Flask = None,
        **kwargs
    ) -> "FlaskRedis": ...

    def init_app(self, app: Flask = None, **kwargs) -> None: ...
