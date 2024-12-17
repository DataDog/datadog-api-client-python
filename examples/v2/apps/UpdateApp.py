"""
Update App returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.apps_api import AppsApi
from datadog_api_client.v2.model.update_app_request import UpdateAppRequest
from datadog_api_client.v2.model.update_app_request_data import UpdateAppRequestData
from datadog_api_client.v2.model.update_app_request_data_attributes import UpdateAppRequestDataAttributes
from datadog_api_client.v2.model.update_app_request_data_type import UpdateAppRequestDataType

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

body = UpdateAppRequest(
    data=UpdateAppRequestData(
        attributes=UpdateAppRequestDataAttributes(
            name="Updated Name",
            root_instance_name="grid0",
        ),
        id=APP_DATA_ID,
        type=UpdateAppRequestDataType.APPDEFINITIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_app"] = True
with ApiClient(configuration) as api_client:
    api_instance = AppsApi(api_client)
    response = api_instance.update_app(app_id=APP_DATA_ID, body=body)

    print(response)
