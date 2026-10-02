# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_impact_user_activity_data import AIImpactUserActivityData


class AIImpactUserActivityRequest(ModelNormal):
    validations = {
        "data": {
            "max_items": 1000,
            "min_items": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_impact_user_activity_data import AIImpactUserActivityData

        return {
            "data": ([AIImpactUserActivityData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[AIImpactUserActivityData], **kwargs):
        """
        Request to send daily AI tool activity for one or more users.

        :param data: A batch of daily AI tool activity entries. A batch must contain between 1 and 1000 entries.
        :type data: [AIImpactUserActivityData]
        """
        super().__init__(kwargs)

        self_.data = data
