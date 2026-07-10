"""
Get postmortem for an incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# there is a valid "postmortem" in the system
POSTMORTEM_DATA_RELATIONSHIPS_INCIDENT_DATA_ID = environ["POSTMORTEM_DATA_RELATIONSHIPS_INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["get_incident_postmortem"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.get_incident_postmortem(
        incident_id=POSTMORTEM_DATA_RELATIONSHIPS_INCIDENT_DATA_ID,
    )

    print(response)
