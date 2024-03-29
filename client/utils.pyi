# Stubs for elasticsearch.client.utils (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..compat import PY2, quote_plus, string_types
from typing import Any

SKIP_IN_PATH: Any
GLOBAL_PARAMS: Any

def query_params(*es_query_params: Any): ...

class NamespacedClient:
    client: Any = ...
    def __init__(self, client: Any) -> None: ...
    @property
    def transport(self): ...

class AddonClient(NamespacedClient):
    @classmethod
    def infect_client(cls, client: Any): ...
