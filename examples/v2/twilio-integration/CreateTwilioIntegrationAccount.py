"""
Create a Twilio integration account returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.twilio_integration_api import TwilioIntegrationApi
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
from datadog_api_client.v2.model.twilio_integration_account_basic_auth_request import (
    TwilioIntegrationAccountBasicAuthRequest,
)
from datadog_api_client.v2.model.twilio_integration_account_basic_auth_type import TwilioIntegrationAccountBasicAuthType
from datadog_api_client.v2.model.twilio_integration_account_create_attributes import (
    TwilioIntegrationAccountCreateAttributes,
)
from datadog_api_client.v2.model.twilio_integration_account_create_data import TwilioIntegrationAccountCreateData
from datadog_api_client.v2.model.twilio_integration_account_create_request import TwilioIntegrationAccountCreateRequest
from datadog_api_client.v2.model.twilio_integration_account_settings_request import (
    TwilioIntegrationAccountSettingsRequest,
)
from datadog_api_client.v2.model.twilio_integration_dataflows_request import TwilioIntegrationDataflowsRequest
from datadog_api_client.v2.model.twilio_messages_logs_integration_dataflow_request import (
    TwilioMessagesLogsIntegrationDataflowRequest,
)

body = TwilioIntegrationAccountCreateRequest(
    data=TwilioIntegrationAccountCreateData(
        attributes=TwilioIntegrationAccountCreateAttributes(
            authentication=TwilioIntegrationAccountBasicAuthRequest(
                auth_type=TwilioIntegrationAccountBasicAuthType.BASIC,
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
            settings=TwilioIntegrationAccountSettingsRequest(
                account_sid="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                censor_logs=True,
            ),
        ),
        type=IntegrationAccountType.INTEGRATION_ACCOUNT,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_twilio_integration_account"] = True
with ApiClient(configuration) as api_client:
    api_instance = TwilioIntegrationApi(api_client)
    response = api_instance.create_twilio_integration_account(body=body)

    print(response)
