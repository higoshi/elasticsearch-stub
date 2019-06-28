# Stubs for elasticsearch.client.nodes (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .utils import NamespacedClient, _make_path, query_params
from typing import Any, Optional

class NodesClient(NamespacedClient):
    def info(self, node_id: Optional[Any] = ..., metric: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def stats(self, node_id: Optional[Any] = ..., metric: Optional[Any] = ..., index_metric: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def hot_threads(self, node_id: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def usage(self, node_id: Optional[Any] = ..., metric: Optional[Any] = ..., params: Optional[Any] = ...): ...