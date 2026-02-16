"""
Create a form version returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.form_version_attributes import FormVersionAttributes
from datadog_api_client.v2.model.form_version_data_request import FormVersionDataRequest
from datadog_api_client.v2.model.form_version_request import FormVersionRequest
from datadog_api_client.v2.model.form_version_state import FormVersionState
from datadog_api_client.v2.model.form_version_type import FormVersionType
from datadog_api_client.v2.model.form_version_upsert_params import FormVersionUpsertParams
from uuid import UUID

body = FormVersionRequest(
    data=FormVersionDataRequest(
        attributes=FormVersionAttributes(
            data_definition=dict([("updated", "true")]),
            state=FormVersionState.DRAFT,
            ui_definition=dict(),
            upsert_params=FormVersionUpsertParams(
                etag="b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d",
                match_policy="none",
            ),
        ),
        type=FormVersionType.FORM_VERSIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_form_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.upsert_form_version(form_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
