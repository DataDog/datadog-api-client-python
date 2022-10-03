"""
Update a RUM application returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_update import RUMApplicationUpdate
from datadog_api_client.v2.model.rum_application_update_attributes import RUMApplicationUpdateAttributes
from datadog_api_client.v2.model.rum_application_update_request import RUMApplicationUpdateRequest
from datadog_api_client.v2.model.rum_application_update_type import RUMApplicationUpdateType

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

body = RUMApplicationUpdateRequest(
    data=RUMApplicationUpdate(
        attributes=RUMApplicationUpdateAttributes(
            name="updated_name_for_my_existing_rum_application",
            type="browser",
        ),
        id=RUM_APPLICATION_DATA_ID,
        type=RUMApplicationUpdateType.RUM_APPLICATION_UPDATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.update_rum_application(id=RUM_APPLICATION_DATA_ID, body=body)

    print(response)
