"""
List On-Call schedules returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    items = api_instance.list_on_call_schedules_with_pagination()
    for item in items:
        print(item)
