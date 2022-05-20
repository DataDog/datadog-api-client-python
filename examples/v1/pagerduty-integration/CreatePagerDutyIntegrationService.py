"""
Create a new service object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.pager_duty_integration_api import PagerDutyIntegrationApi
from datadog_api_client.v1.model.pager_duty_service import PagerDutyService

body = PagerDutyService(
    service_key="",
    service_name="",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PagerDutyIntegrationApi(api_client)
    response = api_instance.create_pager_duty_integration_service(body=body)

    print(response)
