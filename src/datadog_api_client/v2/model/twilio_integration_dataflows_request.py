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
        Dataflows to configure on the Twilio integration account, keyed by dataflow id.

        :param twilio_alerts_logs: The Twilio alerts logs dataflow.
        :type twilio_alerts_logs: TwilioAlertsLogsIntegrationDataflowRequest, optional

        :param twilio_call_summaries_logs: The Twilio call summaries logs dataflow.
        :type twilio_call_summaries_logs: TwilioCallSummariesLogsIntegrationDataflowRequest, optional

        :param twilio_cloud_cost_metrics: The Twilio cloud cost metrics dataflow.
        :type twilio_cloud_cost_metrics: TwilioCloudCostMetricsIntegrationDataflowRequest, optional

        :param twilio_events_logs: The Twilio events logs dataflow.
        :type twilio_events_logs: TwilioEventsLogsIntegrationDataflowRequest, optional

        :param twilio_messages_logs: The Twilio messages logs dataflow.
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
