"""
List ServiceNow assignment groups returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["list_service_now_assignment_groups"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.list_service_now_assignment_groups(
        instance_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
