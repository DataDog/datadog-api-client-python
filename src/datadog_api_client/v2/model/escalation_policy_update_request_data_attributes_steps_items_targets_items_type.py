# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType(ModelSimple):
    """
    Specifies the type of escalation target (example `users`, `schedules`, or `teams`).

    :param value: Must be one of ["users", "schedules", "teams"].
    :type value: str
    """

    allowed_values = {
        "users",
        "schedules",
        "teams",
    }
    USERS: ClassVar["EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType"]
    SCHEDULES: ClassVar["EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType"]
    TEAMS: ClassVar["EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType.USERS = (
    EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType("users")
)
EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType.SCHEDULES = (
    EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType("schedules")
)
EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType.TEAMS = (
    EscalationPolicyUpdateRequestDataAttributesStepsItemsTargetsItemsType("teams")
)
