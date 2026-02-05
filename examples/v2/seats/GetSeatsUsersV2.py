"""
Get seats users for a product code returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.seats_api import SeatsApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SeatsApi(api_client)
    response = api_instance.get_seats_users_v2(
        product_code="product_code",
    )

    print(response)
