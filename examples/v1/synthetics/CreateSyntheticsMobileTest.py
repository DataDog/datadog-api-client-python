"""
Create a mobile test returns "OK - Returns the created test details." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_mobile_test import SyntheticsMobileTest
from datadog_api_client.v1.model.synthetics_mobile_test_config import SyntheticsMobileTestConfig
from datadog_api_client.v1.model.synthetics_mobile_test_options import SyntheticsMobileTestOptions
from datadog_api_client.v1.model.synthetics_mobile_test_type import SyntheticsMobileTestType
from datadog_api_client.v1.model.synthetics_mobile_tests_mobile_application import (
    SyntheticsMobileTestsMobileApplication,
)
from datadog_api_client.v1.model.synthetics_mobile_tests_mobile_application_reference_type import (
    SyntheticsMobileTestsMobileApplicationReferenceType,
)
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus

body = SyntheticsMobileTest(
    name="Example-Synthetic",
    status=SyntheticsTestPauseStatus.PAUSED,
    type=SyntheticsMobileTestType.MOBILE,
    config=SyntheticsMobileTestConfig(
        variables=[],
    ),
    message="",
    options=SyntheticsMobileTestOptions(
        device_ids=[
            "synthetics:mobile:device:iphone_15_ios_17",
        ],
        mobile_application=SyntheticsMobileTestsMobileApplication(
            application_id="ab0e0aed-536d-411a-9a99-5428c27d8f8e",
            reference_id="6115922a-5f5d-455e-bc7e-7955a57f3815",
            reference_type=SyntheticsMobileTestsMobileApplicationReferenceType.VERSION,
        ),
        tick_every=3600,
    ),
    steps=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.create_synthetics_mobile_test(body=body)

    print(response)
