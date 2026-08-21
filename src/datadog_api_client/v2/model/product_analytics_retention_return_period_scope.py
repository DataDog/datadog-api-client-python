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
    from datadog_api_client.v2.model.product_analytics_retention_index_target import (
        ProductAnalyticsRetentionIndexTarget,
    )
    from datadog_api_client.v2.model.product_analytics_retention_return_period_scope_type import (
        ProductAnalyticsRetentionReturnPeriodScopeType,
    )


class ProductAnalyticsRetentionReturnPeriodScope(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_index_target import (
            ProductAnalyticsRetentionIndexTarget,
        )
        from datadog_api_client.v2.model.product_analytics_retention_return_period_scope_type import (
            ProductAnalyticsRetentionReturnPeriodScopeType,
        )

        return {
            "target": (ProductAnalyticsRetentionIndexTarget,),
            "type": (ProductAnalyticsRetentionReturnPeriodScopeType,),
        }

    attribute_map = {
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        target: ProductAnalyticsRetentionIndexTarget,
        type: ProductAnalyticsRetentionReturnPeriodScopeType,
        **kwargs,
    ):
        """
        Narrows a retention query to a single return-period column.

        :param target: Selects a cohort or return period by its zero-based position in the grid.
        :type target: ProductAnalyticsRetentionIndexTarget

        :param type: The discriminator identifying a scope narrowed to one return period.
        :type type: ProductAnalyticsRetentionReturnPeriodScopeType
        """
        super().__init__(kwargs)

        self_.target = target
        self_.type = type
