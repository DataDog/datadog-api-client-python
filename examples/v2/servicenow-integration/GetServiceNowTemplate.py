"""
Get ServiceNow template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["get_service_now_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.get_service_now_template(
        template_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
