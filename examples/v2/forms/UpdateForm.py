"""
Update a form returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.form_type import FormType
from datadog_api_client.v2.model.form_update_attributes import FormUpdateAttributes
from datadog_api_client.v2.model.form_update_attributes_form_update import FormUpdateAttributesFormUpdate
from datadog_api_client.v2.model.form_update_data_request import FormUpdateDataRequest
from datadog_api_client.v2.model.form_update_request import FormUpdateRequest
from uuid import UUID

body = FormUpdateRequest(
    data=FormUpdateDataRequest(
        attributes=FormUpdateAttributes(
            form_update=FormUpdateAttributesFormUpdate(
                description="Updated description",
                name="New Form Name",
            ),
        ),
        id=UUID("00000000-0000-0000-0000-000000000000"),
        type=FormType.FORMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.update_form(form_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
