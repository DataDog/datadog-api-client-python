"""
Update a Statuspage URL setting returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.statuspage_integration_api import StatuspageIntegrationApi
from datadog_api_client.v2.model.statuspage_url_setting_type import StatuspageUrlSettingType
from datadog_api_client.v2.model.statuspage_url_setting_update_attributes import StatuspageUrlSettingUpdateAttributes
from datadog_api_client.v2.model.statuspage_url_setting_update_data import StatuspageUrlSettingUpdateData
from datadog_api_client.v2.model.statuspage_url_setting_update_request import StatuspageUrlSettingUpdateRequest

body = StatuspageUrlSettingUpdateRequest(
    data=StatuspageUrlSettingUpdateData(
        attributes=StatuspageUrlSettingUpdateAttributes(
            custom_tags="team:collaboration-integrations,env:prod",
            url="https://example.statuspage.io",
        ),
        id="596da4af-0563-4097-90ff-07230c3f9db3",
        type=StatuspageUrlSettingType.STATUSPAGE_URL_SETTING,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatuspageIntegrationApi(api_client)
    response = api_instance.update_statuspage_url_setting(
        statuspage_url_setting_id="statuspage_url_setting_id", body=body
    )

    print(response)
