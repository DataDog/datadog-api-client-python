"""
Submit a form returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.form_submission_attributes import FormSubmissionAttributes
from datadog_api_client.v2.model.form_submission_data_request import FormSubmissionDataRequest
from datadog_api_client.v2.model.form_submission_request import FormSubmissionRequest
from datadog_api_client.v2.model.form_submission_type import FormSubmissionType
from uuid import UUID

body = FormSubmissionRequest(
    data=FormSubmissionDataRequest(
        attributes=FormSubmissionAttributes(
            submission_data=dict(),
        ),
        type=FormSubmissionType.FORM_SUBMISSIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["submit_form"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.submit_form(form_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
