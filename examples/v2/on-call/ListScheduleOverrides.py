"""
List On-Call schedule overrides returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.list_schedule_overrides(
        schedule_id=SCHEDULE_DATA_ID,
        filter_start=(datetime.now() + relativedelta(days=-1)),
        filter_end=(datetime.now() + relativedelta(days=2)),
    )

    print(response)
