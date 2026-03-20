"""
Import values for an incident user-defined field returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

configuration = Configuration()
configuration.unstable_operations["import_incident_user_defined_field_values"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.import_incident_user_defined_field_values(
        field_id="00000000-0000-0000-0000-000000000000",
    )

    print(response)
