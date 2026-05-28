"""
Delete a Statuspage URL setting returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.statuspage_integration_api import StatuspageIntegrationApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = StatuspageIntegrationApi(api_client)
    api_instance.delete_statuspage_url_setting(
        statuspage_url_setting_id="statuspage_url_setting_id",
    )
