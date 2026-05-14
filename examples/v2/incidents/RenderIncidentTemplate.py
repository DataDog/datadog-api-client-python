"""
Render an incident template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.incident_render_template_data_attributes_request import (
    IncidentRenderTemplateDataAttributesRequest,
)
from datadog_api_client.v2.model.incident_render_template_data_request import IncidentRenderTemplateDataRequest
from datadog_api_client.v2.model.incident_render_template_request import IncidentRenderTemplateRequest
from datadog_api_client.v2.model.incident_rendered_template_type import IncidentRenderedTemplateType

body = IncidentRenderTemplateRequest(
    data=IncidentRenderTemplateDataRequest(
        attributes=IncidentRenderTemplateDataAttributesRequest(
            content="Incident INC-123 is SEV-1.",
            datetime_format="2006-01-02T15:04:05Z07:00",
            timezone="America/New_York",
            validate_links=False,
            validate_variables=False,
        ),
        type=IncidentRenderedTemplateType.RENDERED_TEMPLATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["render_incident_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.render_incident_template(incident_id="incident_id", body=body)

    print(response)
