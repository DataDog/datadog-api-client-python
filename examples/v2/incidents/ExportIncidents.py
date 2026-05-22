"""
Export incidents returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_search_incidents_export_request import IncidentSearchIncidentsExportRequest

body = IncidentSearchIncidentsExportRequest(
    fields=[
        "title",
        "severity",
        "state",
    ],
    query="state:active",
)

configuration = Configuration()
configuration.unstable_operations["export_incidents"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.export_incidents(body=body)

    print(response.read())
