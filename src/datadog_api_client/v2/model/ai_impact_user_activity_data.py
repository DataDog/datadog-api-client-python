# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_impact_user_activity_attributes import AIImpactUserActivityAttributes
    from datadog_api_client.v2.model.ai_impact_user_activity_type import AIImpactUserActivityType


class AIImpactUserActivityData(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_impact_user_activity_attributes import AIImpactUserActivityAttributes
        from datadog_api_client.v2.model.ai_impact_user_activity_type import AIImpactUserActivityType

        return {
            "attributes": (AIImpactUserActivityAttributes,),
            "type": (AIImpactUserActivityType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AIImpactUserActivityAttributes, type: AIImpactUserActivityType, **kwargs):
        """
        A single daily AI tool activity entry.

        :param attributes: Daily AI coding tool activity for a single user. Each entry reports whether the user was
            active on a given day and which AI tools and models they used.
        :type attributes: AIImpactUserActivityAttributes

        :param type: JSON:API type for AI Impact user activity entries.
        :type type: AIImpactUserActivityType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
