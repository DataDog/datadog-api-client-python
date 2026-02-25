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
    from datadog_api_client.v2.model.product_analytics_audience_account_subquery import (
        ProductAnalyticsAudienceAccountSubquery,
    )
    from datadog_api_client.v2.model.product_analytics_audience_segment_subquery import (
        ProductAnalyticsAudienceSegmentSubquery,
    )
    from datadog_api_client.v2.model.product_analytics_audience_user_subquery import (
        ProductAnalyticsAudienceUserSubquery,
    )


class ProductAnalyticsAudienceFilters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_audience_account_subquery import (
            ProductAnalyticsAudienceAccountSubquery,
        )
        from datadog_api_client.v2.model.product_analytics_audience_segment_subquery import (
            ProductAnalyticsAudienceSegmentSubquery,
        )
        from datadog_api_client.v2.model.product_analytics_audience_user_subquery import (
            ProductAnalyticsAudienceUserSubquery,
        )

        return {
            "accounts": ([ProductAnalyticsAudienceAccountSubquery],),
            "formula": (str,),
            "segments": ([ProductAnalyticsAudienceSegmentSubquery],),
            "users": ([ProductAnalyticsAudienceUserSubquery],),
        }

    attribute_map = {
        "accounts": "accounts",
        "formula": "formula",
        "segments": "segments",
        "users": "users",
    }

    def __init__(
        self_,
        accounts: Union[List[ProductAnalyticsAudienceAccountSubquery], UnsetType] = unset,
        formula: Union[str, UnsetType] = unset,
        segments: Union[List[ProductAnalyticsAudienceSegmentSubquery], UnsetType] = unset,
        users: Union[List[ProductAnalyticsAudienceUserSubquery], UnsetType] = unset,
        **kwargs,
    ):
        """
        Audience filter definitions for targeting specific user segments.

        :param accounts: Account audience queries.
        :type accounts: [ProductAnalyticsAudienceAccountSubquery], optional

        :param formula: Boolean formula combining audience queries by name.
        :type formula: str, optional

        :param segments: Segment audience queries.
        :type segments: [ProductAnalyticsAudienceSegmentSubquery], optional

        :param users: User audience queries.
        :type users: [ProductAnalyticsAudienceUserSubquery], optional
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
