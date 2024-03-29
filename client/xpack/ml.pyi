# Stubs for elasticsearch.client.xpack.ml (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from elasticsearch.client.utils import NamespacedClient
from typing import Any, Optional

class MlClient(NamespacedClient):
    def get_filters(self, filter_id: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def get_datafeeds(self, datafeed_id: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def get_datafeed_stats(self, datafeed_id: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def get_buckets(self, job_id: Any, timestamp: Optional[Any] = ..., body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def post_data(self, job_id: Any, body: Any, params: Optional[Any] = ...): ...
    def stop_datafeed(self, datafeed_id: Any, params: Optional[Any] = ...): ...
    def get_jobs(self, job_id: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def delete_expired_data(self, params: Optional[Any] = ...): ...
    def put_job(self, job_id: Any, body: Any, params: Optional[Any] = ...): ...
    def validate_detector(self, body: Any, params: Optional[Any] = ...): ...
    def start_datafeed(self, datafeed_id: Any, body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def get_records(self, job_id: Any, body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def update_job(self, job_id: Any, body: Any, params: Optional[Any] = ...): ...
    def put_filter(self, filter_id: Any, body: Any, params: Optional[Any] = ...): ...
    def update_datafeed(self, datafeed_id: Any, body: Any, params: Optional[Any] = ...): ...
    def preview_datafeed(self, datafeed_id: Any, params: Optional[Any] = ...): ...
    def flush_job(self, job_id: Any, body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def close_job(self, job_id: Any, params: Optional[Any] = ...): ...
    def open_job(self, job_id: Any, params: Optional[Any] = ...): ...
    def delete_job(self, job_id: Any, params: Optional[Any] = ...): ...
    def forecast_job(self, job_id: Any, params: Optional[Any] = ...): ...
    def update_model_snapshot(self, job_id: Any, snapshot_id: Any, body: Any, params: Optional[Any] = ...): ...
    def delete_filter(self, filter_id: Any, params: Optional[Any] = ...): ...
    def validate(self, body: Any, params: Optional[Any] = ...): ...
    def get_categories(self, job_id: Any, category_id: Optional[Any] = ..., body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def get_influencers(self, job_id: Any, body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def put_datafeed(self, datafeed_id: Any, body: Any, params: Optional[Any] = ...): ...
    def delete_datafeed(self, datafeed_id: Any, params: Optional[Any] = ...): ...
    def get_job_stats(self, job_id: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def revert_model_snapshot(self, job_id: Any, snapshot_id: Any, body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def get_model_snapshots(self, job_id: Any, snapshot_id: Optional[Any] = ..., body: Optional[Any] = ..., params: Optional[Any] = ...): ...
    def delete_model_snapshot(self, job_id: Any, snapshot_id: Any, params: Optional[Any] = ...): ...
