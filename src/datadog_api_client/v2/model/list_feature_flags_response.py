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
    from datadog_api_client.v2.model.feature_flag import FeatureFlag
    from datadog_api_client.v2.model.feature_flags_pagination_meta import FeatureFlagsPaginationMeta


class ListFeatureFlagsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag import FeatureFlag
        from datadog_api_client.v2.model.feature_flags_pagination_meta import FeatureFlagsPaginationMeta

        return {
            "data": ([FeatureFlag],),
            "meta": (FeatureFlagsPaginationMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[FeatureFlag], meta: Union[FeatureFlagsPaginationMeta, UnsetType] = unset, **kwargs):
        """
        Response containing a list of feature flags.

        :param data: List of feature flags.
        :type data: [FeatureFlag]

        :param meta: Pagination metadata for feature flags.
        :type meta: FeatureFlagsPaginationMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
