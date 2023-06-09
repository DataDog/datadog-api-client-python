"""
Schedule a downtime returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi
from datadog_api_client.v2.model.downtime_attribute_create_request import DowntimeAttributeCreateRequest
from datadog_api_client.v2.model.downtime_attribute_monitor_identifier_tags import (
    DowntimeAttributeMonitorIdentifierTags,
)
from datadog_api_client.v2.model.downtime_attribute_schedule_one_time_create_edit_request import (
    DowntimeAttributeScheduleOneTimeCreateEditRequest,
)
from datadog_api_client.v2.model.downtime_create_data import DowntimeCreateData
from datadog_api_client.v2.model.downtime_create_request import DowntimeCreateRequest
from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType

body = DowntimeCreateRequest(
    data=DowntimeCreateData(
        attributes=DowntimeAttributeCreateRequest(
            message="dark forest",
            monitor_identifier=DowntimeAttributeMonitorIdentifierTags(
                monitor_tags=[
                    "cat:hat",
                ],
            ),
            scope="test:exampledowntime",
            schedule=DowntimeAttributeScheduleOneTimeCreateEditRequest(
                start=None,
            ),
        ),
        type=DowntimeResourceType.DOWNTIME,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_downtime"] = True
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.create_downtime(body=body)

    print(response)
