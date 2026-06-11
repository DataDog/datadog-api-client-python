"""
Upsert and publish a form version returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.forms_api import FormsApi
from datadog_api_client.v2.model.form_data_definition import FormDataDefinition
from datadog_api_client.v2.model.form_data_definition_type import FormDataDefinitionType
from datadog_api_client.v2.model.form_ui_definition import FormUiDefinition
from datadog_api_client.v2.model.form_ui_definition_ui_theme import FormUiDefinitionUiTheme
from datadog_api_client.v2.model.form_ui_definition_ui_theme_primary_color import FormUiDefinitionUiThemePrimaryColor
from datadog_api_client.v2.model.form_version_type import FormVersionType
from datadog_api_client.v2.model.upsert_and_publish_form_version_data import UpsertAndPublishFormVersionData
from datadog_api_client.v2.model.upsert_and_publish_form_version_data_attributes import (
    UpsertAndPublishFormVersionDataAttributes,
)
from datadog_api_client.v2.model.upsert_and_publish_form_version_request import UpsertAndPublishFormVersionRequest
from datadog_api_client.v2.model.upsert_and_publish_form_version_upsert_params import (
    UpsertAndPublishFormVersionUpsertParams,
)

# there is a valid "form" in the system
FORM_DATA_ID = environ["FORM_DATA_ID"]

body = UpsertAndPublishFormVersionRequest(
    data=UpsertAndPublishFormVersionData(
        attributes=UpsertAndPublishFormVersionDataAttributes(
            data_definition=FormDataDefinition(
                description="Welcome to the Engineering Experience Survey.",
                required=[],
                title="Developer Experience Survey",
                type=FormDataDefinitionType.OBJECT,
            ),
            ui_definition=FormUiDefinition(
                ui_order=[],
                ui_theme=FormUiDefinitionUiTheme(
                    primary_color=FormUiDefinitionUiThemePrimaryColor.GRAY,
                ),
            ),
            upsert_params=UpsertAndPublishFormVersionUpsertParams(
                etag="b51f08b698d88d8027a935d9db649774949f5fb41a0c559bfee6a9a13225c72d",
            ),
        ),
        type=FormVersionType.FORM_VERSIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_and_publish_form_version"] = True
with ApiClient(configuration) as api_client:
    api_instance = FormsApi(api_client)
    response = api_instance.upsert_and_publish_form_version(form_id=FORM_DATA_ID, body=body)

    print(response)
