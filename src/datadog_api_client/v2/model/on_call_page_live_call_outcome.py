# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnCallPageLiveCallOutcome(ModelSimple):
    """
    The outcome of a live call that has ended.

    :param value: Must be one of ["success_call_answered", "failure_no_responder", "failure_caller_abandoned", "failure_outside_support_hours", "failure_internal_error"].
    :type value: str
    """

    allowed_values = {
        "success_call_answered",
        "failure_no_responder",
        "failure_caller_abandoned",
        "failure_outside_support_hours",
        "failure_internal_error",
    }
    SUCCESS_CALL_ANSWERED: ClassVar["OnCallPageLiveCallOutcome"]
    FAILURE_NO_RESPONDER: ClassVar["OnCallPageLiveCallOutcome"]
    FAILURE_CALLER_ABANDONED: ClassVar["OnCallPageLiveCallOutcome"]
    FAILURE_OUTSIDE_SUPPORT_HOURS: ClassVar["OnCallPageLiveCallOutcome"]
    FAILURE_INTERNAL_ERROR: ClassVar["OnCallPageLiveCallOutcome"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnCallPageLiveCallOutcome.SUCCESS_CALL_ANSWERED = OnCallPageLiveCallOutcome("success_call_answered")
OnCallPageLiveCallOutcome.FAILURE_NO_RESPONDER = OnCallPageLiveCallOutcome("failure_no_responder")
OnCallPageLiveCallOutcome.FAILURE_CALLER_ABANDONED = OnCallPageLiveCallOutcome("failure_caller_abandoned")
OnCallPageLiveCallOutcome.FAILURE_OUTSIDE_SUPPORT_HOURS = OnCallPageLiveCallOutcome("failure_outside_support_hours")
OnCallPageLiveCallOutcome.FAILURE_INTERNAL_ERROR = OnCallPageLiveCallOutcome("failure_internal_error")
