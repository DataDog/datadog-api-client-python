"""
Get a downtime returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

# there is a valid "downtime_v2" in the system
DOWNTIME_V2_DATA_ID = environ["DOWNTIME_V2_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DowntimesApi(api_client)
    response = api_instance.get_downtime(
        downtime_id=DOWNTIME_V2_DATA_ID,
    )

    print(response)
