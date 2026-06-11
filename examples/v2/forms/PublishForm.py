"""
Publish a form version returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.form_publication_type import FormPublicationType
from datadog_api_client.v2.model.publish_form_data import PublishFormData
from datadog_api_client.v2.model.publish_form_data_attributes import PublishFormDataAttributes
from datadog_api_client.v2.model.publish_form_request import PublishFormRequest

# there is a valid "form" in the system
FORM_DATA_ID = environ["FORM_DATA_ID"]

body = PublishFormRequest(
    data=PublishFormData(
        attributes=PublishFormDataAttributes(
            version=1,
        ),
        type=FormPublicationType.FORM_PUBLICATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["publish_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.publish_form(form_id=FORM_DATA_ID, body=body)

    print(response)
