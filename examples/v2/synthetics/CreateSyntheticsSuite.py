"""
Create a test suite returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.synthetics_api import SyntheticsApi
from datadog_api_client.v2.model.suite_create_edit import SuiteCreateEdit
from datadog_api_client.v2.model.suite_create_edit_request import SuiteCreateEditRequest
from datadog_api_client.v2.model.synthetics_suite import SyntheticsSuite
from datadog_api_client.v2.model.synthetics_suite_options import SyntheticsSuiteOptions
from datadog_api_client.v2.model.synthetics_suite_type import SyntheticsSuiteType
from datadog_api_client.v2.model.synthetics_suite_types import SyntheticsSuiteTypes

body = SuiteCreateEditRequest(
    data=SuiteCreateEdit(
        attributes=SyntheticsSuite(
            message="Notification message",
            name="Example suite name",
            options=SyntheticsSuiteOptions(),
            tags=[
                "env:production",
            ],
            tests=[],
            type=SyntheticsSuiteType.SUITE,
        ),
        type=SyntheticsSuiteTypes.SUITES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_synthetics_suite(body=body)

    print(response)
