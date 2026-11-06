"""
Get recovery request progress returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_recovery_api import RUMRecoveryApi
from uuid import UUID

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMRecoveryApi(api_client)
    response = api_instance.get_rum_recovery_request(
        request_id=UUID("11111111-1111-4111-8111-111111111111"),
    )

    print(response)
