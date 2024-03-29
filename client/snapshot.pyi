# Stubs for elasticsearch.client.snapshot (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .utils import NamespacedClient, SKIP_IN_PATH, _make_path, query_params
from typing import Any, Optional

class SnapshotClient(NamespacedClient):
    def create(self, repository: Any, snapshot: Any, body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def delete(self, repository: Any, snapshot: Any, params: Optional[Any] = ...): ...
    def get(self, repository: Any, snapshot: Any, params: Optional[Any] = ...): ...
    def delete_repository(self, repository: Any, params: Optional[Any] = ...): ...
    def get_repository(self, repository: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def create_repository(self, repository: Any, body: Any, params: Optional[Any] = ...): ...
    def restore(self, repository: Any, snapshot: Any, body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def status(self, repository: Optional[Any] = ..., snapshot: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def verify_repository(self, repository: Any, params: Optional[Any] = ...): ...
