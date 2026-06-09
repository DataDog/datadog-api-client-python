"""
Create and publish a form returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.create_form_data import CreateFormData
from datadog_api_client.v2.model.create_form_data_attributes import CreateFormDataAttributes
from datadog_api_client.v2.model.create_form_request import CreateFormRequest
from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
from datadog_api_client.v2.model.form_type import FormType
from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition

body = CreateFormRequest(
    data=CreateFormData(
        attributes=CreateFormDataAttributes(
            anonymous=False,
            data_definition=FormDataDefinition(),
            description="A form to collect user feedback.",
            idp_survey=False,
            name="User Feedback Form",
            single_response=False,
            ui_definition=FormUiDefinition(),
        ),
        type=FormType.FORMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_and_publish_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.create_and_publish_form(body=body)

    print(response)
