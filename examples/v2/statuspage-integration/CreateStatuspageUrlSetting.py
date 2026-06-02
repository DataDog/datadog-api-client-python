"""
Create a Statuspage URL setting returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.statuspage_integration_api import StatuspageIntegrationApi
from datadog_api_client.v2.model.statuspage_url_setting_create_attributes import StatuspageUrlSettingCreateAttributes
from datadog_api_client.v2.model.statuspage_url_setting_create_data import StatuspageUrlSettingCreateData
from datadog_api_client.v2.model.statuspage_url_setting_create_request import StatuspageUrlSettingCreateRequest
from datadog_api_client.v2.model.statuspage_url_setting_type import StatuspageUrlSettingType

body = StatuspageUrlSettingCreateRequest(
    data=StatuspageUrlSettingCreateData(
        attributes=StatuspageUrlSettingCreateAttributes(
            custom_tags="team:collaboration-integrations,env:prod",
            url="https://example.statuspage.io",
        ),
        type=StatuspageUrlSettingType.STATUSPAGE_URL_SETTING,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatuspageIntegrationApi(api_client)
    response = api_instance.create_statuspage_url_setting(body=body)

    print(response)
