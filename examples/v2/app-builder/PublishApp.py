"""
Publish App returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.app_builder_api import AppBuilderApi

# there is a valid "app" in the system
APP_DATA_ID = environ["APP_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AppBuilderApi(api_client)
    response = api_instance.publish_app(
        app_id=APP_DATA_ID,
    )

    print(response)
