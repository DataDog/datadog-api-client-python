"""
Get an incident user-defined field returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["get_incident_user_defined_field"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_user_defined_field(
        field_id="00000000-0000-0000-0000-000000000000",
    )

    print(response)
