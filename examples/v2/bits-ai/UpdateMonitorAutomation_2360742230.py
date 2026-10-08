"""
Enable automatic investigations for a monitor
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_ai_api import BitsAIApi
from datadog_api_client.v2.model.monitor_automation_attributes import MonitorAutomationAttributes
from datadog_api_client.v2.model.monitor_automation_request import MonitorAutomationRequest
from datadog_api_client.v2.model.monitor_automation_request_data import MonitorAutomationRequestData
from datadog_api_client.v2.model.monitor_automation_type import MonitorAutomationType

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

body = MonitorAutomationRequest(
    data=MonitorAutomationRequestData(
        type=MonitorAutomationType.MONITOR_AUTOMATION,
        attributes=MonitorAutomationAttributes(
            enabled=True,
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_monitor_automation"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsAIApi(api_client)
    response = api_instance.update_monitor_automation(monitor_id=int(MONITOR_ID), body=body)

    print(response)
