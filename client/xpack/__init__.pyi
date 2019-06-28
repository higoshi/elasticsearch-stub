# Stubs for elasticsearch.client.xpack (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .deprecation import DeprecationClient
from .graph import GraphClient
from .license import LicenseClient
from .migration import MigrationClient
from .ml import MlClient
from .monitoring import MonitoringClient
from .security import SecurityClient
from .watcher import WatcherClient
from elasticsearch.client.utils import NamespacedClient
from typing import Any, Optional

class XPackClient(NamespacedClient):
    namespace: str = ...
    graph: Any = ...
    license: Any = ...
    monitoring: Any = ...
    security: Any = ...
    watcher: Any = ...
    ml: Any = ...
    migration: Any = ...
    deprecation: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def info(self, params: Optional[Any] = ...): ...
    def usage(self, params: Optional[Any] = ...): ...