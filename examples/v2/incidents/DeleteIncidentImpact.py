"""
Delete an incident impact returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi

# the "incident" has an "incident_impact"
INCIDENT_IMPACT_DATA_ID = environ["INCIDENT_IMPACT_DATA_ID"]
INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID = environ["INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID"]

configuration = Configuration()
configuration.unstable_operations["delete_incident_impact"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    api_instance.delete_incident_impact(
        incident_id=INCIDENT_IMPACT_DATA_RELATIONSHIPS_INCIDENT_DATA_ID,
        impact_id=INCIDENT_IMPACT_DATA_ID,
    )
