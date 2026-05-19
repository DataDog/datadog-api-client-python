# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AutomationRuleTriggerType(ModelSimple):
    """
    The case event that activates the automation rule.

    :param value: Must be one of ["case_created", "status_transitioned", "attribute_value_changed", "event_correlation_signal_correlated", "case_review_approved", "comment_added"].
    :type value: str
    """

    allowed_values = {
        "case_created",
        "status_transitioned",
        "attribute_value_changed",
        "event_correlation_signal_correlated",
        "case_review_approved",
        "comment_added",
    }
    CASE_CREATED: ClassVar["AutomationRuleTriggerType"]
    STATUS_TRANSITIONED: ClassVar["AutomationRuleTriggerType"]
    ATTRIBUTE_VALUE_CHANGED: ClassVar["AutomationRuleTriggerType"]
    EVENT_CORRELATION_SIGNAL_CORRELATED: ClassVar["AutomationRuleTriggerType"]
    CASE_REVIEW_APPROVED: ClassVar["AutomationRuleTriggerType"]
    COMMENT_ADDED: ClassVar["AutomationRuleTriggerType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AutomationRuleTriggerType.CASE_CREATED = AutomationRuleTriggerType("case_created")
AutomationRuleTriggerType.STATUS_TRANSITIONED = AutomationRuleTriggerType("status_transitioned")
AutomationRuleTriggerType.ATTRIBUTE_VALUE_CHANGED = AutomationRuleTriggerType("attribute_value_changed")
AutomationRuleTriggerType.EVENT_CORRELATION_SIGNAL_CORRELATED = AutomationRuleTriggerType(
    "event_correlation_signal_correlated"
)
AutomationRuleTriggerType.CASE_REVIEW_APPROVED = AutomationRuleTriggerType("case_review_approved")
AutomationRuleTriggerType.COMMENT_ADDED = AutomationRuleTriggerType("comment_added")
