"""
Delete Multiple Apps returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi
from datadog_api_client.v2.model.app_definition_type import AppDefinitionType
from datadog_api_client.v2.model.delete_apps_request import DeleteAppsRequest
from datadog_api_client.v2.model.delete_apps_request_data_items import DeleteAppsRequestDataItems

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

body = DeleteAppsRequest(
    data=[
        DeleteAppsRequestDataItems(
            id=APP_DATA_ID,
            type=AppDefinitionType.APPDEFINITIONS,
        ),
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.delete_apps(body=body)

    print(response)
