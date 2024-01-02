"""
Get active downtimes for a monitor returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    items = api_instance.list_monitor_downtimes_with_pagination(
        monitor_id=9223372036854775807,
    )
    for item in items:
        print(item)
