"""
Create backfilled degradation returns "Created" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.status_pages_api import StatusPagesApi
from datadog_api_client.v2.model.create_backfilled_degradation_request import CreateBackfilledDegradationRequest
from datadog_api_client.v2.model.create_backfilled_degradation_request_data import (
    CreateBackfilledDegradationRequestData,
)
from datadog_api_client.v2.model.create_backfilled_degradation_request_data_attributes import (
    CreateBackfilledDegradationRequestDataAttributes,
)
from datadog_api_client.v2.model.create_backfilled_degradation_request_data_attributes_updates_items import (
    CreateBackfilledDegradationRequestDataAttributesUpdatesItems,
)
from datadog_api_client.v2.model.create_degradation_request_data_attributes_components_affected_items import (
    CreateDegradationRequestDataAttributesComponentsAffectedItems,
)
from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
    CreateDegradationRequestDataAttributesStatus,
)
from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType
from datadog_api_client.v2.model.status_pages_component_data_attributes_status import (
    StatusPagesComponentDataAttributesStatus,
)

# there is a valid "status_page" in the system
STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID = environ[
    "STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID"
]
STATUS_PAGE_DATA_ID = environ["STATUS_PAGE_DATA_ID"]

body = CreateBackfilledDegradationRequest(
    data=CreateBackfilledDegradationRequestData(
        attributes=CreateBackfilledDegradationRequestDataAttributes(
            title="Past API Outage",
            updates=[
                CreateBackfilledDegradationRequestDataAttributesUpdatesItems(
                    components_affected=[
                        CreateDegradationRequestDataAttributesComponentsAffectedItems(
                            id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
                            status=StatusPagesComponentDataAttributesStatus.DEGRADED,
                        ),
                    ],
                    description="We detected elevated error rates in the API.",
                    started_at=(datetime.now() + relativedelta(hours=-1)),
                    status=CreateDegradationRequestDataAttributesStatus.INVESTIGATING,
                ),
                CreateBackfilledDegradationRequestDataAttributesUpdatesItems(
                    components_affected=[
                        CreateDegradationRequestDataAttributesComponentsAffectedItems(
                            id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
                            status=StatusPagesComponentDataAttributesStatus.DEGRADED,
                        ),
                    ],
                    description="Root cause identified as a misconfigured deployment.",
                    started_at=(datetime.now() + relativedelta(minutes=-30)),
                    status=CreateDegradationRequestDataAttributesStatus.IDENTIFIED,
                ),
                CreateBackfilledDegradationRequestDataAttributesUpdatesItems(
                    components_affected=[
                        CreateDegradationRequestDataAttributesComponentsAffectedItems(
                            id=STATUS_PAGE_DATA_ATTRIBUTES_COMPONENTS_0_COMPONENTS_0_ID,
                            status=StatusPagesComponentDataAttributesStatus.OPERATIONAL,
                        ),
                    ],
                    description="The issue has been resolved and API is operating normally.",
                    started_at=datetime.now(),
                    status=CreateDegradationRequestDataAttributesStatus.RESOLVED,
                ),
            ],
        ),
        type=PatchDegradationRequestDataType.DEGRADATIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatusPagesApi(api_client)
    response = api_instance.create_backfilled_degradation(page_id=STATUS_PAGE_DATA_ID, body=body)

    print(response)
