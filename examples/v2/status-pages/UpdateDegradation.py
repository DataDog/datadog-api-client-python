"""
Update degradation returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.patch_degradation_request import PatchDegradationRequest
from datadog_api_client.v2.model.patch_degradation_request_data import PatchDegradationRequestData
from datadog_api_client.v2.model.patch_degradation_request_data_attributes import PatchDegradationRequestDataAttributes
from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

# there is a valid "degradation" in the system
DEGRADATION_DATA_ID = environ["DEGRADATION_DATA_ID"]

body = PatchDegradationRequest(
    data=PatchDegradationRequestData(
        attributes=PatchDegradationRequestDataAttributes(
            title="5e2fd69be33e79aa",
        ),
        id=DEGRADATION_DATA_ID,
        type=PatchDegradationRequestDataType.DEGRADATIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.update_degradation(
        page_id=STATUS_PAGE_DATA_ID, degradation_id=DEGRADATION_DATA_ID, body=body
    )

    print(response)
