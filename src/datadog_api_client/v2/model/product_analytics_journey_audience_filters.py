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
    from datadog_api_client.v2.model.product_analytics_journey_audience_account_query import (
        ProductAnalyticsJourneyAudienceAccountQuery,
    )
    from datadog_api_client.v2.model.product_analytics_journey_audience_segment_query import (
        ProductAnalyticsJourneyAudienceSegmentQuery,
    )
    from datadog_api_client.v2.model.product_analytics_journey_audience_user_query import (
        ProductAnalyticsJourneyAudienceUserQuery,
    )


class ProductAnalyticsJourneyAudienceFilters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_journey_audience_account_query import (
            ProductAnalyticsJourneyAudienceAccountQuery,
        )
        from datadog_api_client.v2.model.product_analytics_journey_audience_segment_query import (
            ProductAnalyticsJourneyAudienceSegmentQuery,
        )
        from datadog_api_client.v2.model.product_analytics_journey_audience_user_query import (
            ProductAnalyticsJourneyAudienceUserQuery,
        )

        return {
            "accounts": ([ProductAnalyticsJourneyAudienceAccountQuery],),
            "formula": (str,),
            "segments": ([ProductAnalyticsJourneyAudienceSegmentQuery],),
            "users": ([ProductAnalyticsJourneyAudienceUserQuery],),
        }

    attribute_map = {
        "accounts": "accounts",
        "formula": "formula",
        "segments": "segments",
        "users": "users",
    }

    def __init__(
        self_,
        accounts: Union[List[ProductAnalyticsJourneyAudienceAccountQuery], UnsetType] = unset,
        formula: Union[str, UnsetType] = unset,
        segments: Union[List[ProductAnalyticsJourneyAudienceSegmentQuery], UnsetType] = unset,
        users: Union[List[ProductAnalyticsJourneyAudienceUserQuery], UnsetType] = unset,
        **kwargs,
    ):
        """
        Restricts the journey to an audience built from named sub-queries.
        Sub-query names must be unique across ``users`` , ``segments`` , and ``accounts``.

        :param accounts: Named account sub-queries.
        :type accounts: [ProductAnalyticsJourneyAudienceAccountQuery], optional

        :param formula: Boolean expression combining the sub-query names with ``AND`` , ``OR`` , and ``NOT``.
            When empty, all sub-queries are combined with ``AND``.
        :type formula: str, optional

        :param segments: Named segment sub-queries.
        :type segments: [ProductAnalyticsJourneyAudienceSegmentQuery], optional

        :param users: Named user sub-queries.
        :type users: [ProductAnalyticsJourneyAudienceUserQuery], optional
        """
        if accounts is not unset:
            kwargs["accounts"] = accounts
        if formula is not unset:
            kwargs["formula"] = formula
        if segments is not unset:
            kwargs["segments"] = segments
        if users is not unset:
            kwargs["users"] = users
        super().__init__(kwargs)
