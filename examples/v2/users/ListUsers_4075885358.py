"""
List all users returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.users_api import UsersApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = UsersApi(api_client)
    items = api_instance.list_users_with_pagination(
        page_size=2,
    )
    for item in items:
        print(item)
