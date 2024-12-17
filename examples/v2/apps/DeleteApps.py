"""
Delete Multiple Apps returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apps_api import AppsApi
from datadog_api_client.v2.model.delete_apps_request import DeleteAppsRequest
from datadog_api_client.v2.model.delete_apps_request_data_items import DeleteAppsRequestDataItems
from datadog_api_client.v2.model.delete_apps_request_data_items_type import DeleteAppsRequestDataItemsType

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

body = DeleteAppsRequest(
    data=[
        DeleteAppsRequestDataItems(
            id=APP_DATA_ID,
            type=DeleteAppsRequestDataItemsType.APPDEFINITIONS,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["delete_apps"] = True
with ApiClient(configuration) as api_client:
    api_instance = AppsApi(api_client)
    response = api_instance.delete_apps(body=body)

    print(response)
