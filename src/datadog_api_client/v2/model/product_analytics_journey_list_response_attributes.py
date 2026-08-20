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
    from datadog_api_client.v2.model.product_analytics_journey_entity import ProductAnalyticsJourneyEntity
    from datadog_api_client.v2.model.product_analytics_journey_list_record import ProductAnalyticsJourneyListRecord


class ProductAnalyticsJourneyListResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_entity import ProductAnalyticsJourneyEntity
        from datadog_api_client.v2.model.product_analytics_journey_list_record import ProductAnalyticsJourneyListRecord

        return {
            "entity": (ProductAnalyticsJourneyEntity,),
            "records": ([ProductAnalyticsJourneyListRecord],),
            "total_count": (int,),
        }

    attribute_map = {
        "entity": "entity",
        "records": "records",
        "total_count": "total_count",
    }

    def __init__(
        self_,
        entity: ProductAnalyticsJourneyEntity,
        records: List[ProductAnalyticsJourneyListRecord],
        total_count: int,
        **kwargs,
    ):
        """
        Attributes of a journey list response.

        :param entity: The kind of entity returned by a journey list query.
        :type entity: ProductAnalyticsJourneyEntity

        :param records: The returned rows.
        :type records: [ProductAnalyticsJourneyListRecord]

        :param total_count: Total number of rows matching the query, ignoring ``limit``.
        :type total_count: int
        """
        super().__init__(kwargs)

        self_.entity = entity
        self_.records = records
        self_.total_count = total_count
