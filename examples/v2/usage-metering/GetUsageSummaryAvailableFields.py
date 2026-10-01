"""
Get available fields for usage summary returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.usage_metering_api import UsageMeteringApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = UsageMeteringApi(api_client)
    response = api_instance.get_usage_summary_available_fields()

    attrs = response.data.attributes
    print(f"response_fields ({len(attrs.response_fields)}):")
    for f in attrs.response_fields:
        print(f"  {f}")

    print(f"date_fields ({len(attrs.date_fields)}):")
    for f in attrs.date_fields:
        print(f"  {f}")

    print(f"date_org_fields ({len(attrs.date_org_fields)}):")
    for f in attrs.date_org_fields:
        print(f"  {f}")
