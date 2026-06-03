# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SourcemapsListMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "has_more_results": (bool,),
            "total_filtered_count": (int,),
        }

    attribute_map = {
        "has_more_results": "has_more_results",
        "total_filtered_count": "total_filtered_count",
    }

    def __init__(self_, has_more_results: bool, total_filtered_count: int, **kwargs):
        """
        Page information for the source maps list response.

        :param has_more_results: Whether there are more results available beyond the current page.
        :type has_more_results: bool

        :param total_filtered_count: Total number of source maps matching the filter criteria.
        :type total_filtered_count: int
        """
        super().__init__(kwargs)

        self_.has_more_results = has_more_results
        self_.total_filtered_count = total_filtered_count
