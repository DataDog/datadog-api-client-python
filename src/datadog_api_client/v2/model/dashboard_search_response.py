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
    from datadog_api_client.v2.model.dashboard_search_result_data import DashboardSearchResultData
    from datadog_api_client.v2.model.dashboard_search_response_meta import DashboardSearchResponseMeta


class DashboardSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_search_result_data import DashboardSearchResultData
        from datadog_api_client.v2.model.dashboard_search_response_meta import DashboardSearchResponseMeta

        return {
            "data": ([DashboardSearchResultData],),
            "meta": (DashboardSearchResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[DashboardSearchResultData], meta: DashboardSearchResponseMeta, **kwargs):
        """
        Response containing dashboard search results.

        :param data: List of dashboard search results.
        :type data: [DashboardSearchResultData]

        :param meta: Metadata about the dashboard search results.
        :type meta: DashboardSearchResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
