"""
Update a Twilio integration account returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.twilio_integration_accounts_api import TwilioIntegrationAccountsApi
from datadog_api_client.v2.model.integration_account_basic_auth_type import IntegrationAccountBasicAuthType
from datadog_api_client.v2.model.integration_account_basic_auth_update import IntegrationAccountBasicAuthUpdate
from datadog_api_client.v2.model.integration_account_type import IntegrationAccountType
from datadog_api_client.v2.model.twilio_alerts_logs_integration_dataflow_request import (
    TwilioAlertsLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.twilio_call_summaries_logs_integration_dataflow_request import (
    TwilioCallSummariesLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.twilio_cloud_cost_metrics_integration_dataflow_request import (
    TwilioCloudCostMetricsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.twilio_events_logs_integration_dataflow_request import (
    TwilioEventsLogsIntegrationDataflowRequest,
)
from datadog_api_client.v2.model.twilio_integration_account_settings_update import (
    TwilioIntegrationAccountSettingsUpdate,
)
from datadog_api_client.v2.model.twilio_integration_account_update_attributes import (
    TwilioIntegrationAccountUpdateAttributes,
)
from datadog_api_client.v2.model.twilio_integration_account_update_data import TwilioIntegrationAccountUpdateData
from datadog_api_client.v2.model.twilio_integration_account_update_request import TwilioIntegrationAccountUpdateRequest
from datadog_api_client.v2.model.twilio_integration_dataflows_request import TwilioIntegrationDataflowsRequest
from datadog_api_client.v2.model.twilio_messages_logs_integration_dataflow_request import (
    TwilioMessagesLogsIntegrationDataflowRequest,
)

body = TwilioIntegrationAccountUpdateRequest(
    data=TwilioIntegrationAccountUpdateData(
        attributes=TwilioIntegrationAccountUpdateAttributes(
            authentication=IntegrationAccountBasicAuthUpdate(
                auth_type=IntegrationAccountBasicAuthType.BASIC,
                password="your-password",
                username="datadog",
            ),
            dataflows=TwilioIntegrationDataflowsRequest(
                twilio_alerts_logs=TwilioAlertsLogsIntegrationDataflowRequest(
                    enabled=True,
                ),
                twilio_call_summaries_logs=TwilioCallSummariesLogsIntegrationDataflowRequest(
                    enabled=True,
                ),
                twilio_cloud_cost_metrics=TwilioCloudCostMetricsIntegrationDataflowRequest(
                    enabled=True,
                ),
                twilio_events_logs=TwilioEventsLogsIntegrationDataflowRequest(
                    enabled=True,
                ),
                twilio_messages_logs=TwilioMessagesLogsIntegrationDataflowRequest(
                    enabled=True,
                ),
            ),
            name="twilio-prod",
            settings=TwilioIntegrationAccountSettingsUpdate(
                account_sid="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                censor_logs=True,
            ),
        ),
        id="953a0060-81ec-4221-aed4-d4733b59cd96",
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_twilio_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TwilioIntegrationAccountsApi(api_client)
    response = api_instance.update_twilio_integration_account(account_id="account_id", body=body)

    print(response)
