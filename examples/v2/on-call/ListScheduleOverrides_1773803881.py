"""
List On-Call schedule overrides returns "OK" response with pagination
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi
from datetime import datetime
from dateutil.tz import tzutc

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    items = api_instance.list_schedule_overrides_with_pagination(
        schedule_id="3653d3c6-0c75-11ea-ad28-fb5701eabc7d",
        filter_start=datetime(2024, 1, 7, 2, 53, 1, tzinfo=tzutc()),
        filter_end=datetime(2024, 1, 14, 2, 53, 1, tzinfo=tzutc()),
    )
    for item in items:
        print(item)
