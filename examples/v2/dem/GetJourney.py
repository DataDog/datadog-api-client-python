"""
Get a DEM journey returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dem_api import DEMApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DEMApi(api_client)
    response = api_instance.get_journey(
        journey_id="journey_id",
    )

    print(response)
