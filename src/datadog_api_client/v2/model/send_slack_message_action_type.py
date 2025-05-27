# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SendSlackMessageActionType(ModelSimple):
    """
    Indicates that the action is a send Slack message action.

    :param value: If omitted defaults to "send_slack_message". Must be one of ["send_slack_message"].
    :type value: str
    """

    allowed_values = {
        "send_slack_message",
    }
    SEND_SLACK_MESSAGE: ClassVar["SendSlackMessageActionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SendSlackMessageActionType.SEND_SLACK_MESSAGE = SendSlackMessageActionType("send_slack_message")
