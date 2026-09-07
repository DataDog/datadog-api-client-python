"""
Batch get DEM journeys by test suite IDs returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dem_api import DEMApi
from datadog_api_client.v2.model.dem_batch_get_journeys_attributes import DemBatchGetJourneysAttributes
from datadog_api_client.v2.model.dem_batch_get_journeys_data import DemBatchGetJourneysData
from datadog_api_client.v2.model.dem_batch_get_journeys_request import DemBatchGetJourneysRequest
from datadog_api_client.v2.model.dem_batch_get_journeys_request_type import DemBatchGetJourneysRequestType

body = DemBatchGetJourneysRequest(
    data=DemBatchGetJourneysData(
        attributes=DemBatchGetJourneysAttributes(
            test_suite_ids=[
                "suite-abc123",
                "suite-def456",
            ],
        ),
        type=DemBatchGetJourneysRequestType.BATCH_GET_JOURNEYS_BY_TEST_SUITE_IDS_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DEMApi(api_client)
    response = api_instance.batch_get_journeys_by_test_suite_i_ds(body=body)

    print(response)
