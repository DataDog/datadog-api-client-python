"""
Estimate recoverable sessions returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from datadog_api_client.v2.model.rum_recovery_count_attributes import RumRecoveryCountAttributes
from datadog_api_client.v2.model.rum_recovery_count_request import RumRecoveryCountRequest
from datadog_api_client.v2.model.rum_recovery_count_request_data import RumRecoveryCountRequestData

body = RumRecoveryCountRequest(
    data=RumRecoveryCountRequestData(
        attributes=RumRecoveryCountAttributes(
            _from=1789905600000,
            query="service:web",
            to=1789992000000,
        ),
        id="11111111-1111-4111-8111-111111111111",
        type="rum_recovery_count",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRecoveryApi(api_client)
    response = api_instance.get_rum_recovery_session_count(body=body)

    print(response)
