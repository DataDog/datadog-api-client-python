"""
Clone a form returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.clone_form_data import CloneFormData
from datadog_api_client.v2.model.clone_form_data_attributes import CloneFormDataAttributes
from datadog_api_client.v2.model.clone_form_request import CloneFormRequest
from datadog_api_client.v2.model.form_type import FormType
from uuid import UUID

body = CloneFormRequest(
    data=CloneFormData(
        attributes=CloneFormDataAttributes(
            name="Copy of My Form",
        ),
        type=FormType.FORMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["clone_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.clone_form(form_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
