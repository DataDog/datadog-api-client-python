"""
Create a timestamp override for an incident returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_timestamp_override_create_attributes import (
    IncidentTimestampOverrideCreateAttributes,
)
from datadog_api_client.v2.model.incident_timestamp_override_create_data import IncidentTimestampOverrideCreateData
from datadog_api_client.v2.model.incident_timestamp_override_create_request import (
    IncidentTimestampOverrideCreateRequest,
)
from datadog_api_client.v2.model.incidents_timestamp_overrides_type import IncidentsTimestampOverridesType
from datadog_api_client.v2.model.timestamp_type import TimestampType
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = IncidentTimestampOverrideCreateRequest(
    data=IncidentTimestampOverrideCreateData(
        attributes=IncidentTimestampOverrideCreateAttributes(
            timestamp_type=TimestampType.CREATED,
            timestamp_value=datetime(2024, 12, 29, 10, 0, tzinfo=tzutc()),
        ),
        type=IncidentsTimestampOverridesType.INCIDENTS_TIMESTAMP_OVERRIDES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_incident_timestamp_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_timestamp_override(
        incident_id=UUID("9cecfde8-e35d-4387-8985-9b30dcb9cb1c"), body=body
    )

    print(response)
