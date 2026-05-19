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
    from datadog_api_client.v2.model.case_insight import CaseInsight


class CaseInsightsAttributes(ModelNormal):
    validations = {
        "insights": {
            "max_items": 100,
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_insight import CaseInsight

        return {
            "insights": ([CaseInsight],),
        }

    attribute_map = {
        "insights": "insights",
    }

    def __init__(self_, insights: List[CaseInsight], **kwargs):
        """
        Attributes for adding or removing insights from a case.

        :param insights: Array of insights to add to or remove from a case.
        :type insights: [CaseInsight]
        """
        super().__init__(kwargs)

        self_.insights = insights
