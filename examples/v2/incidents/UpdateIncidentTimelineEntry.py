"""
Update an incident timeline entry returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_timeline_cell_type import IncidentTimelineCellType
from datadog_api_client.v2.model.incident_timeline_entry_content import IncidentTimelineEntryContent
from datadog_api_client.v2.model.incident_timeline_entry_data_attributes_request import (
    IncidentTimelineEntryDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_timeline_entry_data_request import IncidentTimelineEntryDataRequest
from datadog_api_client.v2.model.incident_timeline_entry_request import IncidentTimelineEntryRequest
from datadog_api_client.v2.model.incident_timeline_entry_type import IncidentTimelineEntryType
from datetime import datetime
from dateutil.tz import tzutc
from uuid import UUID

body = IncidentTimelineEntryRequest(
    data=IncidentTimelineEntryDataRequest(
        attributes=IncidentTimelineEntryDataAttributesRequest(
            cell_type=IncidentTimelineCellType.MARKDOWN,
            content=IncidentTimelineEntryContent(
                message="Investigating the issue.",
            ),
            display_time=datetime(2024, 1, 1, 0, 0, tzinfo=tzutc()),
            important=False,
        ),
        type=IncidentTimelineEntryType.INCIDENT_TIMELINE_CELLS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_timeline_entry"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_timeline_entry(
        incident_id="incident_id", timeline_entry_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body
    )

    print(response)
