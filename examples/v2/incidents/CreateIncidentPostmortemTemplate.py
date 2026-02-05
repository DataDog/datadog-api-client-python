"""
Create postmortem template returns "Created" response
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
configuration.unstable_operations["create_incident_postmortem_template"] = True
with ApiClient(configuration) as api_client:
    api_instance = IncidentsApi(api_client)
    response = api_instance.create_incident_postmortem_template(body=body)

    print(response)
