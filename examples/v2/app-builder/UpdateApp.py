"""
Update App returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_definition_type import AppDefinitionType
from datadog_api_client.v2.model.update_app_request import UpdateAppRequest
from datadog_api_client.v2.model.update_app_request_data import UpdateAppRequestData
from datadog_api_client.v2.model.update_app_request_data_attributes import UpdateAppRequestDataAttributes

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

body = UpdateAppRequest(
    data=UpdateAppRequestData(
        attributes=UpdateAppRequestDataAttributes(
            name="Updated Name",
            root_instance_name="grid0",
        ),
        id=APP_DATA_ID,
        type=AppDefinitionType.APPDEFINITIONS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.update_app(app_id=APP_DATA_ID, body=body)

    print(response)
