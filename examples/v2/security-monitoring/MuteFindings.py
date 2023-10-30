"""
Mute or unmute a batch of findings returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.bulk_mute_findings_request import BulkMuteFindingsRequest
from datadog_api_client.v2.model.bulk_mute_findings_request_attributes import BulkMuteFindingsRequestAttributes
from datadog_api_client.v2.model.bulk_mute_findings_request_data import BulkMuteFindingsRequestData
from datadog_api_client.v2.model.bulk_mute_findings_request_meta import BulkMuteFindingsRequestMeta
from datadog_api_client.v2.model.bulk_mute_findings_request_meta_findings import BulkMuteFindingsRequestMetaFindings
from datadog_api_client.v2.model.bulk_mute_findings_request_properties import BulkMuteFindingsRequestProperties
from datadog_api_client.v2.model.finding_mute_reason import FindingMuteReason
from datadog_api_client.v2.model.finding_type import FindingType

body = BulkMuteFindingsRequest(
    data=BulkMuteFindingsRequestData(
        attributes=BulkMuteFindingsRequestAttributes(
            mute=BulkMuteFindingsRequestProperties(
                expiration_date=1778721573794,
                muted=True,
                reason=FindingMuteReason.ACCEPTED_RISK,
            ),
        ),
        id="dbe5f567-192b-4404-b908-29b70e1c9f76",
        meta=BulkMuteFindingsRequestMeta(
            findings=[
                BulkMuteFindingsRequestMetaFindings(
                    finding_id="ZGVmLTAwcC1pZXJ-aS0wZjhjNjMyZDNmMzRlZTgzNw==",
                ),
            ],
        ),
        type=FindingType.FINDING,
    ),
)

configuration = Configuration()
configuration.unstable_operations["mute_findings"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.mute_findings(body=body)

    print(response)
