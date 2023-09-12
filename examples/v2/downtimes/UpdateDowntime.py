"""
Update a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi
from datadog_api_client.v2.model.downtime_resource_type import DowntimeResourceType
from datadog_api_client.v2.model.downtime_update_request import DowntimeUpdateRequest
from datadog_api_client.v2.model.downtime_update_request_attributes import DowntimeUpdateRequestAttributes
from datadog_api_client.v2.model.downtime_update_request_data import DowntimeUpdateRequestData

# there is a valid "downtime_v2" in the system
DOWNTIME_V2_DATA_ID = environ["DOWNTIME_V2_DATA_ID"]

body = DowntimeUpdateRequest(
    data=DowntimeUpdateRequestData(
        attributes=DowntimeUpdateRequestAttributes(
            message="light speed",
        ),
        id=DOWNTIME_V2_DATA_ID,
        type=DowntimeResourceType.DOWNTIME,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.update_downtime(downtime_id=DOWNTIME_V2_DATA_ID, body=body)

    print(response)
