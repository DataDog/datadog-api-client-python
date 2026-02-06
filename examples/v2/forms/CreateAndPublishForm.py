"""
Create and publish a form returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.form_create_request import FormCreateRequest
from datadog_api_client.v2.model.form_data_attributes_request import FormDataAttributesRequest
from datadog_api_client.v2.model.form_data_request import FormDataRequest
from datadog_api_client.v2.model.form_type import FormType
from uuid import UUID

body = FormCreateRequest(
    data=FormDataRequest(
        attributes=FormDataAttributesRequest(
            data_definition=dict(),
            description="test description",
            name="test form happy path",
            ui_definition=dict(),
        ),
        id=UUID("00000000-0000-0000-0000-000000000000"),
        type=FormType.FORMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_and_publish_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.create_and_publish_form(body=body)

    print(response)
