"""
Create a new RUM application returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_create_request import RUMApplicationCreateRequestJSON

body = RUMApplicationCreateRequestJSON(
    name="my_new_rum_application",
    type="ios",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.create_rum_application(body=body)

    print(response)
