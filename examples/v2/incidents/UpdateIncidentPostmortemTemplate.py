"""
Update postmortem template returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.incidents_api import IncidentsApi
from datadog_api_client.v2.model.postmortem_template_attributes_request import PostmortemTemplateAttributesRequest
from datadog_api_client.v2.model.postmortem_template_data_request import PostmortemTemplateDataRequest
from datadog_api_client.v2.model.postmortem_template_request import PostmortemTemplateRequest
from datadog_api_client.v2.model.postmortem_template_type import PostmortemTemplateType

body = PostmortemTemplateRequest(
    data=PostmortemTemplateDataRequest(
        attributes=PostmortemTemplateAttributesRequest(
            name="Standard Postmortem Template",
        ),
        type=PostmortemTemplateType.POSTMORTEM_TEMPLATE,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_incident_postmortem_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.update_incident_postmortem_template(template_id="template-456", body=body)

    print(response)
