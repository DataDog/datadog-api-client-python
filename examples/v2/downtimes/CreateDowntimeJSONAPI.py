"""
Schedule a downtime returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi
from datadog_api_client.v2.model.downtime_create_request import DowntimeCreateRequestJSON
from datadog_api_client.v2.model.downtime_monitor_identifier_tags import DowntimeMonitorIdentifierTags
from datadog_api_client.v2.model.downtime_schedule_one_time_create_update_request import (
    DowntimeScheduleOneTimeCreateUpdateRequest,
)

body = DowntimeCreateRequestJSON(
    message="dark forest",
    monitor_identifier=DowntimeMonitorIdentifierTags(
        monitor_tags=[
            "cat:hat",
        ],
    ),
    scope="test:exampledowntime",
    schedule=DowntimeScheduleOneTimeCreateUpdateRequest(
        start=None,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_downtime"] = True
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
