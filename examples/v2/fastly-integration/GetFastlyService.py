"""
Get Fastly service returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.fastly_integration_api import FastlyIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = FastlyIntegrationApi(api_client)
    response = api_instance.get_fastly_service(
        account_id="account_id",
        service_id="service_id",
    )

    print(response)
