"""
Delete a single service object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.opsgenie_integration_api import OpsgenieIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OpsgenieIntegrationApi(api_client)
    api_instance.delete_opsgenie_service(
        integration_service_id="integration_service_id",
    )
