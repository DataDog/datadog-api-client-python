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
    from datadog_api_client.v2.model.product_analytics_journey_computed_column_name import (
        ProductAnalyticsJourneyComputedColumnName,
    )


class ProductAnalyticsJourneyComputedColumn(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_computed_column_name import (
            ProductAnalyticsJourneyComputedColumnName,
        )

        return {
            "name": (ProductAnalyticsJourneyComputedColumnName,),
        }

    attribute_map = {
        "name": "name",
    }

    def __init__(self_, name: ProductAnalyticsJourneyComputedColumnName, **kwargs):
        """
        A computed column added to each row. Requesting ``first_conversion_timestamps`` adds one
        ``<node alias>_timestamp`` key per step.

        :param name: Name of a computed column to add to each row.
        :type name: ProductAnalyticsJourneyComputedColumnName
        """
        super().__init__(kwargs)

        self_.name = name
