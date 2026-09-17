"""
Trigger a Bits AI investigation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_ai_api import BitsAIApi
from datadog_api_client.v2.model.monitor_alert_trigger import MonitorAlertTrigger
from datadog_api_client.v2.model.monitor_alert_trigger_attributes import MonitorAlertTriggerAttributes
from datadog_api_client.v2.model.monitor_alert_trigger_type import MonitorAlertTriggerType
from datadog_api_client.v2.model.trigger_investigation_request import TriggerInvestigationRequest
from datadog_api_client.v2.model.trigger_investigation_request_data import TriggerInvestigationRequestData
from datadog_api_client.v2.model.trigger_investigation_request_data_attributes import (
    TriggerInvestigationRequestDataAttributes,
)
from datadog_api_client.v2.model.trigger_investigation_request_type import TriggerInvestigationRequestType

body = TriggerInvestigationRequest(
    data=TriggerInvestigationRequestData(
        attributes=TriggerInvestigationRequestDataAttributes(
            trigger=MonitorAlertTrigger(
                monitor_alert_trigger=MonitorAlertTriggerAttributes(
                    event_id="1234567890123456789",
                    event_ts=1700000000000,
                    monitor_id=12345678,
                ),
                type=MonitorAlertTriggerType.MONITOR_ALERT_TRIGGER,
            ),
        ),
        type=TriggerInvestigationRequestType.TRIGGER_INVESTIGATION_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["trigger_investigation"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsAIApi(api_client)
    response = api_instance.trigger_investigation(body=body)

    print(response)
