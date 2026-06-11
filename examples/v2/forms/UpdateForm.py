"""
Update a form returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.form_datastore_config_attributes import FormDatastoreConfigAttributes
from datadog_api_client.v2.model.form_type import FormType
from datadog_api_client.v2.model.form_update_attributes import FormUpdateAttributes
from datadog_api_client.v2.model.update_form_data import UpdateFormData
from datadog_api_client.v2.model.update_form_data_attributes import UpdateFormDataAttributes
from datadog_api_client.v2.model.update_form_request import UpdateFormRequest
from uuid import UUID

# there is a valid "form" in the system
FORM_DATA_ID = environ["FORM_DATA_ID"]

body = UpdateFormRequest(
    data=UpdateFormData(
        attributes=UpdateFormDataAttributes(
            form_update=FormUpdateAttributes(
                datastore_config=FormDatastoreConfigAttributes(
                    datastore_id=UUID("5108ea24-dd83-4696-9caa-f069f73d0fad"),
                    primary_column_name="id",
                    primary_key_generation_strategy="none",
                ),
                description="An updated description.",
                name="Updated Form Name",
            ),
        ),
        id=FORM_DATA_ID,
        type=FormType.FORMS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.update_form(form_id=FORM_DATA_ID, body=body)

    print(response)
