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
    from datadog_api_client.v2.model.feature_flag_history_pagination_meta_page import (
        FeatureFlagHistoryPaginationMetaPage,
    )


class FeatureFlagHistoryPaginationMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.feature_flag_history_pagination_meta_page import (
            FeatureFlagHistoryPaginationMetaPage,
        )

        return {
            "page": (FeatureFlagHistoryPaginationMetaPage,),
        }

    attribute_map = {
        "page": "page",
    }

    def __init__(self_, page: Union[FeatureFlagHistoryPaginationMetaPage, UnsetType] = unset, **kwargs):
        """
        Pagination metadata for feature flag change history.

        :param page: Pagination metadata for feature flag change history responses.
        :type page: FeatureFlagHistoryPaginationMetaPage, optional
        """
        if page is not unset:
            kwargs["page"] = page
        super().__init__(kwargs)
