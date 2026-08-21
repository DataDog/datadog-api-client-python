# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_retention_grid_cohort import ProductAnalyticsRetentionGridCohort
    from datadog_api_client.v2.model.product_analytics_retention_period import ProductAnalyticsRetentionPeriod
    from datadog_api_client.v2.model.product_analytics_unit import ProductAnalyticsUnit


class ProductAnalyticsRetentionGridResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_grid_cohort import (
            ProductAnalyticsRetentionGridCohort,
        )
        from datadog_api_client.v2.model.product_analytics_retention_period import ProductAnalyticsRetentionPeriod
        from datadog_api_client.v2.model.product_analytics_unit import ProductAnalyticsUnit

        return {
            "cohorts": ([ProductAnalyticsRetentionGridCohort],),
            "retention_entity": (str,),
            "retention_periods": ([ProductAnalyticsRetentionPeriod],),
            "unit": ([ProductAnalyticsUnit],),
        }

    attribute_map = {
        "cohorts": "cohorts",
        "retention_entity": "retention_entity",
        "retention_periods": "retention_periods",
        "unit": "unit",
    }

    def __init__(
        self_,
        cohorts: Union[List[ProductAnalyticsRetentionGridCohort], UnsetType] = unset,
        retention_entity: Union[str, UnsetType] = unset,
        retention_periods: Union[List[ProductAnalyticsRetentionPeriod], UnsetType] = unset,
        unit: Union[List[ProductAnalyticsUnit], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a retention grid response, containing the cohort rows and the period columns.

        :param cohorts: The cohorts forming the rows of the grid.
        :type cohorts: [ProductAnalyticsRetentionGridCohort], optional

        :param retention_entity: The entity whose retention was measured.
        :type retention_entity: str, optional

        :param retention_periods: The return periods forming the columns of the grid.
        :type retention_periods: [ProductAnalyticsRetentionPeriod], optional

        :param unit: Unit definitions for the grid values.
        :type unit: [ProductAnalyticsUnit], optional
        """
        if cohorts is not unset:
            kwargs["cohorts"] = cohorts
        if retention_entity is not unset:
            kwargs["retention_entity"] = retention_entity
        if retention_periods is not unset:
            kwargs["retention_periods"] = retention_periods
        if unit is not unset:
            kwargs["unit"] = unit
        super().__init__(kwargs)
