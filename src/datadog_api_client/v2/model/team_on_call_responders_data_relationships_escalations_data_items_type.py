# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType(ModelSimple):
    """
    Escalation policy steps resource type.

    :param value: If omitted defaults to "escalation_policy_steps". Must be one of ["escalation_policy_steps"].
    :type value: str
    """

    allowed_values = {
        "escalation_policy_steps",
    }
    ESCALATION_POLICY_STEPS: ClassVar["TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType.ESCALATION_POLICY_STEPS = (
    TeamOnCallRespondersDataRelationshipsEscalationsDataItemsType("escalation_policy_steps")
)
