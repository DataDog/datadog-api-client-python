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

    :param value: Must be one of ["CASE_CREATED", "STATUS_TRANSITIONED", "ATTRIBUTE_VALUE_CHANGED", "EVENT_CORRELATION_SIGNAL_CORRELATED", "CASE_REVIEW_APPROVED", "COMMENT_ADDED"].
    :type value: str
    """

    allowed_values = {
        "CASE_CREATED",
        "STATUS_TRANSITIONED",
        "ATTRIBUTE_VALUE_CHANGED",
        "EVENT_CORRELATION_SIGNAL_CORRELATED",
        "CASE_REVIEW_APPROVED",
        "COMMENT_ADDED",
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


AutomationRuleTriggerType.CASE_CREATED = AutomationRuleTriggerType("CASE_CREATED")
AutomationRuleTriggerType.STATUS_TRANSITIONED = AutomationRuleTriggerType("STATUS_TRANSITIONED")
AutomationRuleTriggerType.ATTRIBUTE_VALUE_CHANGED = AutomationRuleTriggerType("ATTRIBUTE_VALUE_CHANGED")
AutomationRuleTriggerType.EVENT_CORRELATION_SIGNAL_CORRELATED = AutomationRuleTriggerType(
    "EVENT_CORRELATION_SIGNAL_CORRELATED"
)
AutomationRuleTriggerType.CASE_REVIEW_APPROVED = AutomationRuleTriggerType("CASE_REVIEW_APPROVED")
AutomationRuleTriggerType.COMMENT_ADDED = AutomationRuleTriggerType("COMMENT_ADDED")
