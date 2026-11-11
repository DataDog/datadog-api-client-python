"""
Get the details of an incident includes responders with modification timestamps
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_related_object import IncidentRelatedObject

# there is a valid "incident_with_commander" in the system
INCIDENT_WITH_COMMANDER_DATA_ID = environ["INCIDENT_WITH_COMMANDER_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_incident"] = True
configuration.unstable_operations["get_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident(
        incident_id=INCIDENT_WITH_COMMANDER_DATA_ID,
        include=[
            IncidentRelatedObject.RESPONDERS,
        ],
    )

    print(response)
