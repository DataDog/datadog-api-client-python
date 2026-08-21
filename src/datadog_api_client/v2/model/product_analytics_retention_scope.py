# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ProductAnalyticsRetentionScope(ModelComposed):
    def __init__(self, **kwargs):
        """
        Restricts a retention query to part of the grid, so that results can be examined in detail.
        Omit it to compute the whole grid.

        :param target: Selects a cohort, either by index or by the aggregation that rolls all cohorts together.
        :type target: ProductAnalyticsRetentionCohortTarget

        :param type: The discriminator identifying a scope narrowed to one cohort.
        :type type: ProductAnalyticsRetentionCohortScopeType

        :param cohort_target: Selects a cohort, either by index or by the aggregation that rolls all cohorts together.
        :type cohort_target: ProductAnalyticsRetentionCohortTarget

        :param return_period_target: Selects a cohort or return period by its zero-based position in the grid.
        :type return_period_target: ProductAnalyticsRetentionIndexTarget
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.product_analytics_retention_cohort_scope import (
            ProductAnalyticsRetentionCohortScope,
        )
        from datadog_api_client.v2.model.product_analytics_retention_return_period_scope import (
            ProductAnalyticsRetentionReturnPeriodScope,
        )
        from datadog_api_client.v2.model.product_analytics_retention_cell_scope import (
            ProductAnalyticsRetentionCellScope,
        )

        return {
            "oneOf": [
                ProductAnalyticsRetentionCohortScope,
                ProductAnalyticsRetentionReturnPeriodScope,
                ProductAnalyticsRetentionCellScope,
            ],
        }
