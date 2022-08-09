"""
Delete a RUM application returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    api_instance.delete_rum_application(
        id=RUM_APPLICATION_DATA_ID,
    )
