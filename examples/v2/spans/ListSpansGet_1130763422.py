"""
Get a list of spans returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_api import SpansApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = SpansApi(api_client)
    items = api_instance.list_spans_get_with_pagination(
        page_limit=2,
    )
    for item in items:
        print(item)
