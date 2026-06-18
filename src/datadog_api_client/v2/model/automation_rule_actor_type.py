# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AutomationRuleActorType(ModelSimple):
    """
    Whether the actor is a user or the Datadog system.

    :param value: Must be one of ["user", "system"].
    :type value: str
    """

    allowed_values = {
        "user",
        "system",
    }
    USER: ClassVar["AutomationRuleActorType"]
    SYSTEM: ClassVar["AutomationRuleActorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AutomationRuleActorType.USER = AutomationRuleActorType("user")
AutomationRuleActorType.SYSTEM = AutomationRuleActorType("system")
