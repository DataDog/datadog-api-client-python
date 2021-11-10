"""
Get a list of incidents returns "OK" response
"""

from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

with ApiClient(Configuration()) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.list_incidents()

    print(response)
