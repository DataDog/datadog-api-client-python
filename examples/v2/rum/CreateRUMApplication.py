"""
Create a new RUM application returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_create import RUMApplicationCreate
from datadog_api_client.v2.model.rum_application_create_attributes import RUMApplicationCreateAttributes
from datadog_api_client.v2.model.rum_application_create_request import RUMApplicationCreateRequest
from datadog_api_client.v2.model.rum_application_create_type import RUMApplicationCreateType

body = RUMApplicationCreateRequest(
    data=RUMApplicationCreate(
        attributes=RUMApplicationCreateAttributes(
            name="my_new_rum_application",
            type="ios",
        ),
        type=RUMApplicationCreateType.RUM_APPLICATION_CREATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.create_rum_application(body=body)

    print(response)
