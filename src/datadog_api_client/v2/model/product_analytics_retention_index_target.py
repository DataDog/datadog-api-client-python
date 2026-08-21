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
    from datadog_api_client.v2.model.product_analytics_retention_index_target_type import (
        ProductAnalyticsRetentionIndexTargetType,
    )


class ProductAnalyticsRetentionIndexTarget(ModelNormal):
    validations = {
        "value": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_index_target_type import (
            ProductAnalyticsRetentionIndexTargetType,
        )

        return {
            "type": (ProductAnalyticsRetentionIndexTargetType,),
            "value": (int,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self_, type: ProductAnalyticsRetentionIndexTargetType, value: int, **kwargs):
        """
        Selects a cohort or return period by its zero-based position in the grid.

        :param type: The discriminator identifying a target selected by index.
        :type type: ProductAnalyticsRetentionIndexTargetType

        :param value: Zero-based index of the targeted cohort or return period.
        :type value: int
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
