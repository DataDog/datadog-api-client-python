"""
Update an existing incident returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
from datadog_api_client.v2.model.incident_field_attributes_single_value_type import (
    IncidentFieldAttributesSingleValueType,
)
from datadog_api_client.v2.model.incident_type import IncidentType
from datadog_api_client.v2.model.incident_update_attributes import IncidentUpdateAttributes
from datadog_api_client.v2.model.incident_update_data import IncidentUpdateData
from datadog_api_client.v2.model.incident_update_request import IncidentUpdateRequest

# there is a valid "incident" in the system
INCIDENT_DATA_ATTRIBUTES_TITLE = environ["INCIDENT_DATA_ATTRIBUTES_TITLE"]
INCIDENT_DATA_ID = environ["INCIDENT_DATA_ID"]

body = IncidentUpdateRequest(
    data=IncidentUpdateData(
        id=INCIDENT_DATA_ID,
        type=IncidentType.INCIDENTS,
        attributes=IncidentUpdateAttributes(
            fields=dict(
                state=IncidentFieldAttributesSingleValue(
                    type=IncidentFieldAttributesSingleValueType.DROPDOWN,
                    value="resolved",
                ),
            ),
            title="A test incident title-updated",
        ),
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident(incident_id=INCIDENT_DATA_ID, body=body)

    print(response)
