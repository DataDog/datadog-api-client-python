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
    from datadog_api_client.v2.model.product_analytics_retention_cohort_scope_type import (
        ProductAnalyticsRetentionCohortScopeType,
    )
    from datadog_api_client.v2.model.product_analytics_retention_index_target import (
        ProductAnalyticsRetentionIndexTarget,
    )
    from datadog_api_client.v2.model.product_analytics_retention_aggregation_target import (
        ProductAnalyticsRetentionAggregationTarget,
    )


class ProductAnalyticsRetentionCohortScope(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_cohort_target import (
            ProductAnalyticsRetentionCohortTarget,
        )
        from datadog_api_client.v2.model.product_analytics_retention_cohort_scope_type import (
            ProductAnalyticsRetentionCohortScopeType,
        )

        return {
            "target": (ProductAnalyticsRetentionCohortTarget,),
            "type": (ProductAnalyticsRetentionCohortScopeType,),
        }

    attribute_map = {
        "target": "target",
        "type": "type",
    }

    def __init__(
        self_,
        target: Union[
            ProductAnalyticsRetentionCohortTarget,
            ProductAnalyticsRetentionIndexTarget,
            ProductAnalyticsRetentionAggregationTarget,
        ],
        type: ProductAnalyticsRetentionCohortScopeType,
        **kwargs,
    ):
        """
        Narrows a retention query to a single cohort row.

        :param target: Selects a cohort, either by index or by the aggregation that rolls all cohorts together.
        :type target: ProductAnalyticsRetentionCohortTarget

        :param type: The discriminator identifying a scope narrowed to one cohort.
        :type type: ProductAnalyticsRetentionCohortScopeType
        """
        super().__init__(kwargs)

        self_.target = target
        self_.type = type
