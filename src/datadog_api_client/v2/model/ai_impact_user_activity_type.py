# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AIImpactUserActivityType(ModelSimple):
    """
    JSON:API type for AI Impact user activity entries.

    :param value: If omitted defaults to "ai_impact_user_activity". Must be one of ["ai_impact_user_activity"].
    :type value: str
    """

    allowed_values = {
        "ai_impact_user_activity",
    }
    AI_IMPACT_USER_ACTIVITY: ClassVar["AIImpactUserActivityType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AIImpactUserActivityType.AI_IMPACT_USER_ACTIVITY = AIImpactUserActivityType("ai_impact_user_activity")
