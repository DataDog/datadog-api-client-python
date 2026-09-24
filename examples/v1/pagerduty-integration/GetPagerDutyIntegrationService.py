"""
Get a single service object returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.pager_duty_integration_api import PagerDutyIntegrationApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = PagerDutyIntegrationApi(api_client)
    response = api_instance.get_pager_duty_integration_service(
        service_name="service_name",
    )

    print(response)
