"""
Publish a form returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.form_publication_attributes import FormPublicationAttributes
from datadog_api_client.v2.model.form_publication_data_request import FormPublicationDataRequest
from datadog_api_client.v2.model.form_publication_request import FormPublicationRequest
from datadog_api_client.v2.model.form_publication_type import FormPublicationType
from uuid import UUID

body = FormPublicationRequest(
    data=FormPublicationDataRequest(
        attributes=FormPublicationAttributes(
            version=1,
        ),
        type=FormPublicationType.FORM_PUBLICATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["publish_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.publish_form(form_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
