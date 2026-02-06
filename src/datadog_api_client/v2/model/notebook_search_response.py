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
    from datadog_api_client.v2.model.notebook_search_result_data import NotebookSearchResultData
    from datadog_api_client.v2.model.notebook_search_response_meta import NotebookSearchResponseMeta


class NotebookSearchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notebook_search_result_data import NotebookSearchResultData
        from datadog_api_client.v2.model.notebook_search_response_meta import NotebookSearchResponseMeta

        return {
            "data": ([NotebookSearchResultData],),
            "meta": (NotebookSearchResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[NotebookSearchResultData], meta: NotebookSearchResponseMeta, **kwargs):
        """
        Response containing notebook search results.

        :param data: List of notebook search results.
        :type data: [NotebookSearchResultData]

        :param meta: Metadata about the notebook search results.
        :type meta: NotebookSearchResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
