# Stubs for elasticsearch.connection.base (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..exceptions import HTTP_EXCEPTIONS, TransportError
from typing import Any, Optional

logger: Any
tracer: Any

class Connection:
    use_ssl: Any = ...
    host: Any = ...
    url_prefix: Any = ...
    timeout: Any = ...
    def __init__(self, host: str = ..., port: int = ..., use_ssl: bool = ..., url_prefix: str = ..., timeout: int = ..., **kwargs: Any) -> None: ...
    def log_request_success(self, method: Any, full_url: Any, path: Any, body: Any, status_code: Any, response: Any, duration: Any) -> None: ...
    def log_request_fail(self, method: Any, full_url: Any, path: Any, body: Any, duration: Any, status_code: Optional[Any] = ..., response: Optional[Any] = ..., exception: Optional[Any] = ...) -> None: ...
