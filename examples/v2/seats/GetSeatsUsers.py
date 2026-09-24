"""
Get users with seats returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.seats_api import SeatsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = SeatsApi(api_client)
    response = api_instance.get_seats_users(
        product_code="incident_response",
        page_limit=100,
    )

    print(response)
