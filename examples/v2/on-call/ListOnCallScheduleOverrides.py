"""
Get a list of all overrides for a schedule returns "OK" response
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "schedule" in the system
SCHEDULE_DATA_ID = environ["SCHEDULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.list_on_call_schedule_overrides(
        schedule_id=SCHEDULE_DATA_ID,
        filter_start=(datetime.now() + relativedelta(hours=-1)),
        filter_end=(datetime.now() + relativedelta(hours=1)),
    )

    print(response)
