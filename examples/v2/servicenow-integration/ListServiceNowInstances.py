"""
List ServiceNow instances returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.service_now_integration_api import ServiceNowIntegrationApi

configuration = Configuration()
configuration.unstable_operations["list_service_now_instances"] = True
with ApiClient(configuration) as api_client:
    api_instance = ServiceNowIntegrationApi(api_client)
    response = api_instance.list_service_now_instances()

    print(response)
