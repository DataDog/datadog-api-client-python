"""
Upsert incident automation data returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_automation_data_attributes_request import (
    IncidentAutomationDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_automation_data_data_request import IncidentAutomationDataDataRequest
from datadog_api_client.v2.model.incident_automation_data_request import IncidentAutomationDataRequest
from datadog_api_client.v2.model.incident_automation_data_type import IncidentAutomationDataType

body = IncidentAutomationDataRequest(
    data=IncidentAutomationDataDataRequest(
        attributes=IncidentAutomationDataAttributesRequest(
            value="completed",
        ),
        type=IncidentAutomationDataType.INCIDENTS_AUTOMATION_DATA,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_incident_automation_data"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.upsert_incident_automation_data(incident_id="incident_id", key="key", body=body)

    print(response)
