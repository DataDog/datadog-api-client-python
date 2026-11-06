"""
Create a recovery request returns "Accepted" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from datadog_api_client.v2.model.rum_recovery_create_data import RumRecoveryCreateData
from datadog_api_client.v2.model.rum_recovery_create_request import RumRecoveryCreateRequest
from datadog_api_client.v2.model.rum_recovery_session_input import RumRecoverySessionInput
from datadog_api_client.v2.model.rum_recovery_sessions_create_attributes import RumRecoverySessionsCreateAttributes
from datadog_api_client.v2.model.rum_recovery_sessions_request_type import RumRecoverySessionsRequestType
from uuid import UUID

body = RumRecoveryCreateRequest(
    data=RumRecoveryCreateData(
        attributes=RumRecoverySessionsCreateAttributes(
            request_type=RumRecoverySessionsRequestType.SESSIONS,
            sessions=[
                RumRecoverySessionInput(
                    application_id=UUID("a33671aa-24fd-4dcd-ba4b-5bbdbafe7690"),
                    session_id=UUID("00000000-0000-4000-8000-000000000001"),
                ),
            ],
        ),
        type="rum_recovery_request",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRecoveryApi(api_client)
    response = api_instance.create_rum_recovery_request(body=body)

    print(response)
