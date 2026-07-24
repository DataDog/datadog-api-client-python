"""
Update postmortem for an incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_postmortem_type import IncidentPostmortemType
from datadog_api_client.v2.model.incident_postmortem_update_attributes import IncidentPostmortemUpdateAttributes
from datadog_api_client.v2.model.incident_postmortem_update_data import IncidentPostmortemUpdateData
from datadog_api_client.v2.model.incident_postmortem_update_request import IncidentPostmortemUpdateRequest
from datadog_api_client.v2.model.postmortem_status import PostmortemStatus

# there is a valid "postmortem" in the system
POSTMORTEM_DATA_ID = environ["POSTMORTEM_DATA_ID"]
POSTMORTEM_DATA_RELATIONSHIPS_INCIDENT_DATA_ID = environ["POSTMORTEM_DATA_RELATIONSHIPS_INCIDENT_DATA_ID"]

body = IncidentPostmortemUpdateRequest(
    data=IncidentPostmortemUpdateData(
        attributes=IncidentPostmortemUpdateAttributes(
            status=PostmortemStatus.IN_REVIEW,
        ),
        id=POSTMORTEM_DATA_ID,
        type=IncidentPostmortemType.INCIDENT_POSTMORTEMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_postmortem"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_postmortem(
        incident_id=POSTMORTEM_DATA_RELATIONSHIPS_INCIDENT_DATA_ID, body=body
    )

    print(response)
