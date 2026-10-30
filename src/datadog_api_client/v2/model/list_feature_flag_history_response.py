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
    from datadog_api_client.v2.model.feature_flag_change_event import FeatureFlagChangeEvent
    from datadog_api_client.v2.model.feature_flags_pagination_links import FeatureFlagsPaginationLinks
    from datadog_api_client.v2.model.feature_flag_history_pagination_meta import FeatureFlagHistoryPaginationMeta


class ListFeatureFlagHistoryResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_change_event import FeatureFlagChangeEvent
        from datadog_api_client.v2.model.feature_flags_pagination_links import FeatureFlagsPaginationLinks
        from datadog_api_client.v2.model.feature_flag_history_pagination_meta import FeatureFlagHistoryPaginationMeta

        return {
            "data": ([FeatureFlagChangeEvent],),
            "links": (FeatureFlagsPaginationLinks,),
            "meta": (FeatureFlagHistoryPaginationMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: List[FeatureFlagChangeEvent],
        links: Union[FeatureFlagsPaginationLinks, UnsetType] = unset,
        meta: Union[FeatureFlagHistoryPaginationMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response containing feature flag change events, newest first.

        :param data: The change events.
        :type data: [FeatureFlagChangeEvent]

        :param links: Pagination links. Follow ``next`` with the same authentication to retrieve the next page. Links use ``page[limit]`` and ``page[offset]`` and preserve the filters. Navigation links are omitted when not applicable.
        :type links: FeatureFlagsPaginationLinks, optional

        :param meta: Pagination metadata for feature flag change history.
        :type meta: FeatureFlagHistoryPaginationMeta, optional
        """
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
