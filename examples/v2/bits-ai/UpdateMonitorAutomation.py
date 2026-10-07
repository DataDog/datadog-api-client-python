"""
Update monitor automatic investigation settings returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_ai_api import BitsAIApi
from datadog_api_client.v2.model.monitor_automation_attributes import MonitorAutomationAttributes
from datadog_api_client.v2.model.monitor_automation_request import MonitorAutomationRequest
from datadog_api_client.v2.model.monitor_automation_request_data import MonitorAutomationRequestData
from datadog_api_client.v2.model.monitor_automation_type import MonitorAutomationType

body = MonitorAutomationRequest(
    data=MonitorAutomationRequestData(
        attributes=MonitorAutomationAttributes(
            enabled=True,
        ),
        type=MonitorAutomationType.MONITOR_AUTOMATION,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_monitor_automation"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsAIApi(api_client)
    response = api_instance.update_monitor_automation(monitor_id=9223372036854775807, body=body)

    print(response)
