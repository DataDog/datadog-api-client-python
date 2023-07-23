"""
Mute or unmute a finding returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.finding_mute_reason import FindingMuteReason
from datadog_api_client.v2.model.mute_finding_request import MuteFindingRequestJSON
from datadog_api_client.v2.model.mute_finding_request_properties import MuteFindingRequestProperties

body = MuteFindingRequestJSON(
    id="AQAAAYbb1i0gijTHEQAAAABBWWJiMWkwZ0FBQ2FuNzBJVGZXZ3B3QUE",
    mute=MuteFindingRequestProperties(
        description="To be resolved later",
        expiration_date=1778721573794,
        muted=True,
        reason=FindingMuteReason.ACCEPTED_RISK,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_finding"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.update_finding(
        finding_id="AQAAAYbb1i0gijTHEQAAAABBWWJiMWkwZ0FBQ2FuNzBJVGZXZ3B3QUE", body=body
    )

    print(response)
