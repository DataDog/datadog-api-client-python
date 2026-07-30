# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TwilioDataflowId(ModelSimple):
    """
    Identifier of a Twilio dataflow.

    :param value: Must be one of ["twilio-cloud-cost-metrics", "twilio-events-logs", "twilio-messages-logs", "twilio-alerts-logs", "twilio-call-summaries-logs"].
    :type value: str
    """

    allowed_values = {
        "twilio-cloud-cost-metrics",
        "twilio-events-logs",
        "twilio-messages-logs",
        "twilio-alerts-logs",
        "twilio-call-summaries-logs",
    }
    CLOUD_COST_METRICS: ClassVar["TwilioDataflowId"]
    EVENTS_LOGS: ClassVar["TwilioDataflowId"]
    MESSAGES_LOGS: ClassVar["TwilioDataflowId"]
    ALERTS_LOGS: ClassVar["TwilioDataflowId"]
    CALL_SUMMARIES_LOGS: ClassVar["TwilioDataflowId"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TwilioDataflowId.CLOUD_COST_METRICS = TwilioDataflowId("twilio-cloud-cost-metrics")
TwilioDataflowId.EVENTS_LOGS = TwilioDataflowId("twilio-events-logs")
TwilioDataflowId.MESSAGES_LOGS = TwilioDataflowId("twilio-messages-logs")
TwilioDataflowId.ALERTS_LOGS = TwilioDataflowId("twilio-alerts-logs")
TwilioDataflowId.CALL_SUMMARIES_LOGS = TwilioDataflowId("twilio-call-summaries-logs")
