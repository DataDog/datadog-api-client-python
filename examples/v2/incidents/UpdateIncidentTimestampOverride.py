"""
Update a timestamp override for an incident returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_timestamp_override_patch_attributes import (
    IncidentTimestampOverridePatchAttributes,
)
from datadog_api_client.v2.model.incident_timestamp_override_patch_data import IncidentTimestampOverridePatchData
from datadog_api_client.v2.model.incident_timestamp_override_patch_request import IncidentTimestampOverridePatchRequest
from datadog_api_client.v2.model.incidents_timestamp_overrides_type import IncidentsTimestampOverridesType
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = IncidentTimestampOverridePatchRequest(
    data=IncidentTimestampOverridePatchData(
        attributes=IncidentTimestampOverridePatchAttributes(
            timestamp_value=datetime(2024, 12, 29, 11, 0, tzinfo=tzutc()),
        ),
        type=IncidentsTimestampOverridesType.INCIDENTS_TIMESTAMP_OVERRIDES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_timestamp_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_timestamp_override(
        incident_id=UUID("9cecfde8-e35d-4387-8985-9b30dcb9cb1c"),
        timestamp_override_id=UUID("6f48a86f-9a39-4bcf-a76b-9a1b20188995"),
        body=body,
    )

    print(response)
