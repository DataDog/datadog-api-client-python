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
    from datadog_api_client.v1.model.product_analytics_audience_account_subquery import (
        ProductAnalyticsAudienceAccountSubquery,
    )
    from datadog_api_client.v1.model.product_analytics_audience_segment_subquery import (
        ProductAnalyticsAudienceSegmentSubquery,
    )
    from datadog_api_client.v1.model.product_analytics_audience_user_subquery import (
        ProductAnalyticsAudienceUserSubquery,
    )


class ProductAnalyticsAudienceFilters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.product_analytics_audience_account_subquery import (
            ProductAnalyticsAudienceAccountSubquery,
        )
        from datadog_api_client.v1.model.product_analytics_audience_segment_subquery import (
            ProductAnalyticsAudienceSegmentSubquery,
        )
        from datadog_api_client.v1.model.product_analytics_audience_user_subquery import (
            ProductAnalyticsAudienceUserSubquery,
        )

        return {
            "accounts": ([ProductAnalyticsAudienceAccountSubquery],),
            "filter_condition": (str,),
            "segments": ([ProductAnalyticsAudienceSegmentSubquery],),
            "users": ([ProductAnalyticsAudienceUserSubquery],),
        }

    attribute_map = {
        "accounts": "accounts",
        "filter_condition": "filter_condition",
        "segments": "segments",
        "users": "users",
    }

    def __init__(
        self_,
        accounts: Union[List[ProductAnalyticsAudienceAccountSubquery], UnsetType] = unset,
        filter_condition: Union[str, UnsetType] = unset,
        segments: Union[List[ProductAnalyticsAudienceSegmentSubquery], UnsetType] = unset,
        users: Union[List[ProductAnalyticsAudienceUserSubquery], UnsetType] = unset,
        **kwargs,
    ):
        """
        Product Analytics/RUM audience filters.

        :param accounts:
        :type accounts: [ProductAnalyticsAudienceAccountSubquery], optional

        :param filter_condition:
        :type filter_condition: str, optional

        :param segments:
        :type segments: [ProductAnalyticsAudienceSegmentSubquery], optional

        :param users:
        :type users: [ProductAnalyticsAudienceUserSubquery], optional
        """
        if accounts is not unset:
            kwargs["accounts"] = accounts
        if filter_condition is not unset:
            kwargs["filter_condition"] = filter_condition
        if segments is not unset:
            kwargs["segments"] = segments
        if users is not unset:
            kwargs["users"] = users
        super().__init__(kwargs)
