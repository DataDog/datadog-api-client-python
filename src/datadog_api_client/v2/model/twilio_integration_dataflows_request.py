# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
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
    from datadog_api_client.v2.model.twilio_messages_logs_integration_dataflow_request import (
        TwilioMessagesLogsIntegrationDataflowRequest,
    )


class TwilioIntegrationDataflowsRequest(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
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
        from datadog_api_client.v2.model.twilio_messages_logs_integration_dataflow_request import (
            TwilioMessagesLogsIntegrationDataflowRequest,
        )

        return {
            "twilio_alerts_logs": (TwilioAlertsLogsIntegrationDataflowRequest,),
            "twilio_call_summaries_logs": (TwilioCallSummariesLogsIntegrationDataflowRequest,),
            "twilio_cloud_cost_metrics": (TwilioCloudCostMetricsIntegrationDataflowRequest,),
            "twilio_events_logs": (TwilioEventsLogsIntegrationDataflowRequest,),
            "twilio_messages_logs": (TwilioMessagesLogsIntegrationDataflowRequest,),
        }

    attribute_map = {
        "twilio_alerts_logs": "twilio-alerts-logs",
        "twilio_call_summaries_logs": "twilio-call-summaries-logs",
        "twilio_cloud_cost_metrics": "twilio-cloud-cost-metrics",
        "twilio_events_logs": "twilio-events-logs",
        "twilio_messages_logs": "twilio-messages-logs",
    }

    def __init__(
        self_,
        twilio_alerts_logs: Union[TwilioAlertsLogsIntegrationDataflowRequest, UnsetType] = unset,
        twilio_call_summaries_logs: Union[TwilioCallSummariesLogsIntegrationDataflowRequest, UnsetType] = unset,
        twilio_cloud_cost_metrics: Union[TwilioCloudCostMetricsIntegrationDataflowRequest, UnsetType] = unset,
        twilio_events_logs: Union[TwilioEventsLogsIntegrationDataflowRequest, UnsetType] = unset,
        twilio_messages_logs: Union[TwilioMessagesLogsIntegrationDataflowRequest, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data Datadog collects from Twilio, keyed by dataflow id. Each dataflow turns on a distinct kind of collection: set ``enabled`` to start or stop it. Defaults listed on each dataflow apply when the account is created; on update, omitted fields keep their current values. Where a dataflow depends on a Twilio feature being enabled, that prerequisite is noted on the dataflow; a dataflow enabled without it is stored but collects no data.

        :param twilio_alerts_logs: Twilio Alert resource logs, which detail the errors and warnings raised when Twilio makes a webhook request to your server or when your application calls the Twilio REST API. This is the one kind of data the integration collects by default.
        :type twilio_alerts_logs: TwilioAlertsLogsIntegrationDataflowRequest, optional

        :param twilio_call_summaries_logs: Twilio Call Summary resource logs, covering the metadata and performance of the calls made from your Twilio account. Requires Voice Insights Advanced Features to be enabled on the Twilio account; without it this dataflow collects no data.
        :type twilio_call_summaries_logs: TwilioCallSummariesLogsIntegrationDataflowRequest, optional

        :param twilio_cloud_cost_metrics: Your Twilio cost data, so that Twilio spend can be broken down and attributed in `Cloud Cost Management <https://docs.datadoghq.com/cloud_cost_management/>`_. Cost data appears in Cloud Cost Management within 24 hours of enabling this dataflow.
        :type twilio_cloud_cost_metrics: TwilioCloudCostMetricsIntegrationDataflowRequest, optional

        :param twilio_events_logs: Twilio Event resource logs, which record virtually every action taken in your Twilio account, such as provisioning a phone number, changing account security settings, or deleting a recording. Actions are recorded whether they came from the REST API, a user in the Twilio Console, or Twilio itself. `Cloud SIEM <https://docs.datadoghq.com/security/cloud_siem/>`_ analyzes and correlates these logs to detect threats in real time.
        :type twilio_events_logs: TwilioEventsLogsIntegrationDataflowRequest, optional

        :param twilio_messages_logs: Twilio Message resource logs for inbound and outbound messages, used to track delivery and troubleshoot message errors. A log is produced when you send a message through the REST API, when Twilio executes a TwiML instruction, and when someone messages one of your Twilio numbers or channel addresses. Message bodies are never collected.
        :type twilio_messages_logs: TwilioMessagesLogsIntegrationDataflowRequest, optional
        """
        if twilio_alerts_logs is not unset:
            kwargs["twilio_alerts_logs"] = twilio_alerts_logs
        if twilio_call_summaries_logs is not unset:
            kwargs["twilio_call_summaries_logs"] = twilio_call_summaries_logs
        if twilio_cloud_cost_metrics is not unset:
            kwargs["twilio_cloud_cost_metrics"] = twilio_cloud_cost_metrics
        if twilio_events_logs is not unset:
            kwargs["twilio_events_logs"] = twilio_events_logs
        if twilio_messages_logs is not unset:
            kwargs["twilio_messages_logs"] = twilio_messages_logs
        super().__init__(kwargs)
