"""
Cancel a batch recovery request returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from datadog_api_client.v2.model.rum_recovery_cancel_attributes import RumRecoveryCancelAttributes
from datadog_api_client.v2.model.rum_recovery_cancel_data import RumRecoveryCancelData
from datadog_api_client.v2.model.rum_recovery_cancel_request import RumRecoveryCancelRequest
from datadog_api_client.v2.model.rum_recovery_cancel_status import RumRecoveryCancelStatus
from uuid import UUID

body = RumRecoveryCancelRequest(
    data=RumRecoveryCancelData(
        attributes=RumRecoveryCancelAttributes(
            status=RumRecoveryCancelStatus.CANCELLED,
        ),
        id="11111111-1111-4111-8111-111111111111",
        type="rum_recovery_request",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRecoveryApi(api_client)
    response = api_instance.update_rum_recovery_batch_request(
        request_id=UUID("11111111-1111-4111-8111-111111111111"), body=body
    )

    print(response)
