"""
Create an incident returns "CREATED" response using JSON:API models
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_create_request import IncidentCreateRequestJSON
from datadog_api_client.v2.model.incident_field_attributes_single_value import IncidentFieldAttributesSingleValue
from datadog_api_client.v2.model.incident_field_attributes_single_value_type import (
    IncidentFieldAttributesSingleValueType,
)

# there is a valid "user" in the system
USER_DATA_ID = environ["USER_DATA_ID"]

body = IncidentCreateRequestJSON(
    title="Example-Incident",
    customer_impacted=False,
    fields=dict(
        state=IncidentFieldAttributesSingleValue(
            type=IncidentFieldAttributesSingleValueType.DROPDOWN,
            value="resolved",
        ),
    ),
    commander_user="string",
)

configuration = Configuration()
configuration.unstable_operations["create_incident"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident(body=body)

    print(response)
