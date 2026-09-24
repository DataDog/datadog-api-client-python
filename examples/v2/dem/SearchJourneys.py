"""
Search DEM journeys returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dem_api import DEMApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = DEMApi(api_client)
    response = api_instance.search_journeys()

    print(response)
