"""
Get incident automation data returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["get_incident_automation_data"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_automation_data(
        incident_id="incident_id",
        key="key",
    )

    print(response)
