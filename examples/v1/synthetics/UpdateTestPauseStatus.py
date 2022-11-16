"""
Pause or start a test returns "OK - Returns a boolean indicating if the update was successful." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.synthetics_api import SyntheticsApi
from datadog_api_client.v1.model.synthetics_test_pause_status import SyntheticsTestPauseStatus
from datadog_api_client.v1.model.synthetics_update_test_pause_status_payload import (
    SyntheticsUpdateTestPauseStatusPayload,
)

body = SyntheticsUpdateTestPauseStatusPayload(
    new_status=SyntheticsTestPauseStatus.LIVE,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SyntheticsApi(api_client)
    response = api_instance.update_test_pause_status(public_id="public_id", body=body)

    print(response)
