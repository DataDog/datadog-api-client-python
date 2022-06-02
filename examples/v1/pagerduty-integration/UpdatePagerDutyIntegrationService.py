"""
Update a single service object returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.pager_duty_integration_api import PagerDutyIntegrationApi
from datadog_api_client.v1.model.pager_duty_service_key import PagerDutyServiceKey

body = PagerDutyServiceKey(
    service_key="",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PagerDutyIntegrationApi(api_client)
    api_instance.update_pager_duty_integration_service(service_name="service_name", body=body)
