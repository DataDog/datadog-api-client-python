"""
Cancel a batch recovery request returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from datadog_api_client.v2.model.rum_recovery_cancel_attributes import RUMRecoveryCancelAttributes
from datadog_api_client.v2.model.rum_recovery_cancel_data import RUMRecoveryCancelData
from datadog_api_client.v2.model.rum_recovery_cancel_request import RUMRecoveryCancelRequest
from datadog_api_client.v2.model.rum_recovery_cancel_status import RUMRecoveryCancelStatus
from uuid import UUID

body = RUMRecoveryCancelRequest(
    data=RUMRecoveryCancelData(
        attributes=RUMRecoveryCancelAttributes(
            status=RUMRecoveryCancelStatus.CANCELLED,
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
