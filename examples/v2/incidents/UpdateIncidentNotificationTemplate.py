"""
Update incident notification template returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_notification_template_type import IncidentNotificationTemplateType
from datadog_api_client.v2.model.incident_notification_template_update_attributes import (
    IncidentNotificationTemplateUpdateAttributes,
)
from datadog_api_client.v2.model.incident_notification_template_update_data import (
    IncidentNotificationTemplateUpdateData,
)
from datadog_api_client.v2.model.patch_incident_notification_template_request import (
    PatchIncidentNotificationTemplateRequest,
)

# there is a valid "notification_template" in the system
NOTIFICATION_TEMPLATE_DATA_ID = environ["NOTIFICATION_TEMPLATE_DATA_ID"]

body = PatchIncidentNotificationTemplateRequest(
    data=IncidentNotificationTemplateUpdateData(
        attributes=IncidentNotificationTemplateUpdateAttributes(
            category="update",
            content="Incident Status Update:\n\nTitle: Sample Incident Title\nNew Status: resolved\nSeverity: SEV-2\nServices: web-service, database-service\nCommander: John Doe\n\nFor more details, visit the incident page.",
            name="Example-Incident",
            subject="Incident Update: Sample Incident Title - resolved",
        ),
        id=NOTIFICATION_TEMPLATE_DATA_ID,
        type=IncidentNotificationTemplateType.NOTIFICATION_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_notification_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_notification_template(id=NOTIFICATION_TEMPLATE_DATA_ID, body=body)

    print(response)
