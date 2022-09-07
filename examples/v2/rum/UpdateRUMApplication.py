"""
Update a RUM application returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.rum_application_update import RUMApplicationUpdate
from datadog_api_client.v2.model.rum_application_update_attributes import RUMApplicationUpdateAttributes
from datadog_api_client.v2.model.rum_application_update_request import RUMApplicationUpdateRequest
from datadog_api_client.v2.model.rum_application_update_type import RUMApplicationUpdateType

body = RUMApplicationUpdateRequest(
    data=RUMApplicationUpdate(
        attributes=RUMApplicationUpdateAttributes(
            name="updated_name_for_my_existing_rum_application",
            type="browser",
        ),
        id="abcd1234-0000-0000-abcd-1234abcd5678",
        type=RUMApplicationUpdateType.RUM_APPLICATION_UPDATE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.update_rum_application(id="id", body=body)

    print(response)
