# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_retention_cohort_target import (
        ProductAnalyticsRetentionCohortTarget,
    )
    from datadog_api_client.v2.model.product_analytics_retention_index_target import (
        ProductAnalyticsRetentionIndexTarget,
    )
    from datadog_api_client.v2.model.product_analytics_retention_cell_scope_type import (
        ProductAnalyticsRetentionCellScopeType,
    )
    from datadog_api_client.v2.model.product_analytics_retention_index_target import (
        ProductAnalyticsRetentionIndexTarget,
    )
    from datadog_api_client.v2.model.product_analytics_retention_aggregation_target import (
        ProductAnalyticsRetentionAggregationTarget,
    )


class ProductAnalyticsRetentionCellScope(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_cohort_target import (
            ProductAnalyticsRetentionCohortTarget,
        )
        from datadog_api_client.v2.model.product_analytics_retention_index_target import (
            ProductAnalyticsRetentionIndexTarget,
        )
        from datadog_api_client.v2.model.product_analytics_retention_cell_scope_type import (
            ProductAnalyticsRetentionCellScopeType,
        )

        return {
            "cohort_target": (ProductAnalyticsRetentionCohortTarget,),
            "return_period_target": (ProductAnalyticsRetentionIndexTarget,),
            "type": (ProductAnalyticsRetentionCellScopeType,),
        }

    attribute_map = {
        "cohort_target": "cohort_target",
        "return_period_target": "return_period_target",
        "type": "type",
    }

    def __init__(
        self_,
        cohort_target: Union[
            ProductAnalyticsRetentionCohortTarget,
            ProductAnalyticsRetentionIndexTarget,
            ProductAnalyticsRetentionAggregationTarget,
        ],
        return_period_target: ProductAnalyticsRetentionIndexTarget,
        type: ProductAnalyticsRetentionCellScopeType,
        **kwargs,
    ):
        """
        Narrows a retention query to a single cell, at the intersection of one cohort and one return period.

        :param cohort_target: Selects a cohort, either by index or by the aggregation that rolls all cohorts together.
        :type cohort_target: ProductAnalyticsRetentionCohortTarget

        :param return_period_target: Selects a cohort or return period by its zero-based position in the grid.
        :type return_period_target: ProductAnalyticsRetentionIndexTarget

        :param type: The discriminator identifying a scope narrowed to one grid cell.
        :type type: ProductAnalyticsRetentionCellScopeType
        """
        super().__init__(kwargs)

        self_.cohort_target = cohort_target
        self_.return_period_target = return_period_target
        self_.type = type
