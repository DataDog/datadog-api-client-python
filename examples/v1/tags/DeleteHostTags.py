"""
Remove host tags returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.tags_api import TagsApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = TagsApi(api_client)
    api_instance.delete_host_tags(
        host_name="host_name",
    )
