# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_retention_cohort_criteria import (
        ProductAnalyticsRetentionCohortCriteria,
    )
    from datadog_api_client.v2.model.product_analytics_retention_filters import ProductAnalyticsRetentionFilters
    from datadog_api_client.v2.model.product_analytics_retention_entity import ProductAnalyticsRetentionEntity
    from datadog_api_client.v2.model.product_analytics_retention_return_condition import (
        ProductAnalyticsRetentionReturnCondition,
    )
    from datadog_api_client.v2.model.product_analytics_retention_return_criteria import (
        ProductAnalyticsRetentionReturnCriteria,
    )


class ProductAnalyticsRetentionSearch(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_cohort_criteria import (
            ProductAnalyticsRetentionCohortCriteria,
        )
        from datadog_api_client.v2.model.product_analytics_retention_filters import ProductAnalyticsRetentionFilters
        from datadog_api_client.v2.model.product_analytics_retention_entity import ProductAnalyticsRetentionEntity
        from datadog_api_client.v2.model.product_analytics_retention_return_condition import (
            ProductAnalyticsRetentionReturnCondition,
        )
        from datadog_api_client.v2.model.product_analytics_retention_return_criteria import (
            ProductAnalyticsRetentionReturnCriteria,
        )

        return {
            "cohort_criteria": (ProductAnalyticsRetentionCohortCriteria,),
            "filters": (ProductAnalyticsRetentionFilters,),
            "retention_entity": (ProductAnalyticsRetentionEntity,),
            "return_condition": (ProductAnalyticsRetentionReturnCondition,),
            "return_criteria": (ProductAnalyticsRetentionReturnCriteria,),
        }

    attribute_map = {
        "cohort_criteria": "cohort_criteria",
        "filters": "filters",
        "retention_entity": "retention_entity",
        "return_condition": "return_condition",
        "return_criteria": "return_criteria",
    }

    def __init__(
        self_,
        cohort_criteria: ProductAnalyticsRetentionCohortCriteria,
        retention_entity: ProductAnalyticsRetentionEntity,
        return_condition: ProductAnalyticsRetentionReturnCondition,
        filters: Union[ProductAnalyticsRetentionFilters, UnsetType] = unset,
        return_criteria: Union[ProductAnalyticsRetentionReturnCriteria, UnsetType] = unset,
        **kwargs,
    ):
        """
        Defines the cohort and return criteria that make up a retention query.

        :param cohort_criteria: Defines the event that places an entity into a cohort, and how cohorts are bucketed over time.
        :type cohort_criteria: ProductAnalyticsRetentionCohortCriteria

        :param filters: Filters narrowing the events considered by a retention query.
        :type filters: ProductAnalyticsRetentionFilters, optional

        :param retention_entity: The entity whose retention is measured.
        :type retention_entity: ProductAnalyticsRetentionEntity

        :param return_condition: When an entity counts as having returned. Use ``conversion_on`` to count only entities that
            returned during the period itself, or ``conversion_on_or_after`` to also count later returns.
        :type return_condition: ProductAnalyticsRetentionReturnCondition

        :param return_criteria: Defines the event that counts as a return, and the window in which it must occur.
        :type return_criteria: ProductAnalyticsRetentionReturnCriteria, optional
        """
        if filters is not unset:
            kwargs["filters"] = filters
        if return_criteria is not unset:
            kwargs["return_criteria"] = return_criteria
        super().__init__(kwargs)

        self_.cohort_criteria = cohort_criteria
        self_.retention_entity = retention_entity
        self_.return_condition = return_condition
