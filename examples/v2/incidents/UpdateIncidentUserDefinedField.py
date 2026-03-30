"""
Update an incident user-defined field returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_user_defined_field_attributes_update_request import (
    IncidentUserDefinedFieldAttributesUpdateRequest,
)
from datadog_api_client.v2.model.incident_user_defined_field_category import IncidentUserDefinedFieldCategory
from datadog_api_client.v2.model.incident_user_defined_field_collected import IncidentUserDefinedFieldCollected
from datadog_api_client.v2.model.incident_user_defined_field_type import IncidentUserDefinedFieldType
from datadog_api_client.v2.model.incident_user_defined_field_update_data import IncidentUserDefinedFieldUpdateData
from datadog_api_client.v2.model.incident_user_defined_field_update_request import IncidentUserDefinedFieldUpdateRequest
from datadog_api_client.v2.model.incident_user_defined_field_valid_value import IncidentUserDefinedFieldValidValue

body = IncidentUserDefinedFieldUpdateRequest(
    data=IncidentUserDefinedFieldUpdateData(
        attributes=IncidentUserDefinedFieldAttributesUpdateRequest(
            category=IncidentUserDefinedFieldCategory.WHAT_HAPPENED,
            collected=IncidentUserDefinedFieldCollected.ACTIVE,
            default_value="critical",
            display_name="Root Cause",
            ordinal="1.5",
            required=False,
            valid_values=[
                IncidentUserDefinedFieldValidValue(
                    description="A critical severity incident.",
                    display_name="Critical",
                    short_description="Critical",
                    value="critical",
                ),
            ],
        ),
        id="00000000-0000-0000-0000-000000000000",
        type=IncidentUserDefinedFieldType.USER_DEFINED_FIELD,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_user_defined_field"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_user_defined_field(
        field_id="00000000-0000-0000-0000-000000000000", body=body
    )

    print(response)
