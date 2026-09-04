"""
Create a test suite for a DEM journey returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dem_api import DEMApi
from datadog_api_client.v2.model.dem_create_journey_test_suite_attributes import DemCreateJourneyTestSuiteAttributes
from datadog_api_client.v2.model.dem_create_journey_test_suite_data import DemCreateJourneyTestSuiteData
from datadog_api_client.v2.model.dem_create_journey_test_suite_request import DemCreateJourneyTestSuiteRequest
from datadog_api_client.v2.model.dem_create_journey_test_suite_request_type import DemCreateJourneyTestSuiteRequestType

body = DemCreateJourneyTestSuiteRequest(
    data=DemCreateJourneyTestSuiteData(
        attributes=DemCreateJourneyTestSuiteAttributes(
            include_tests_from_journey_coverage=True,
            test_suite_name="My Custom Suite",
        ),
        type=DemCreateJourneyTestSuiteRequestType.CREATE_TEST_SUITE_FOR_JOURNEY_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DEMApi(api_client)
    response = api_instance.create_test_suite_for_journey(public_journey_id="public_journey_id", body=body)

    print(response)
