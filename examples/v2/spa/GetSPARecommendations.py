"""
Get SPA Recommendations returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spa_api import SpaApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_spa_recommendations"] = True
with ApiClient(configuration) as api_client:
    api_instance = SpaApi(api_client)
    response = api_instance.get_spa_recommendations(
        service="service",
    )

    print(response)
