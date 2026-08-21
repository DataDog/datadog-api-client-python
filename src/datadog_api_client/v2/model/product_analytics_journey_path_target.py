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
    from datadog_api_client.v2.model.product_analytics_journey_path_target_type import (
        ProductAnalyticsJourneyPathTargetType,
    )


class ProductAnalyticsJourneyPathTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_path_target_type import (
            ProductAnalyticsJourneyPathTargetType,
        )

        return {
            "end": (str,),
            "start": (str,),
            "type": (ProductAnalyticsJourneyPathTargetType,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
        "type": "type",
    }

    def __init__(self_, end: str, start: str, type: ProductAnalyticsJourneyPathTargetType, **kwargs):
        """
        A reference to the range of steps between two nodes of the journey.

        :param end: Alias of the node the path ends at.
        :type end: str

        :param start: Alias of the node the path starts at.
        :type start: str

        :param type: The discriminator identifying a target that references a range of steps.
        :type type: ProductAnalyticsJourneyPathTargetType
        """
        super().__init__(kwargs)

        self_.end = end
        self_.start = start
        self_.type = type
