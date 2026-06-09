# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CsmUnifiedHostsMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "page_index": (int,),
            "page_size": (int,),
            "total_filtered": (int,),
            "total_pages": (int,),
        }

    attribute_map = {
        "page_index": "page_index",
        "page_size": "page_size",
        "total_filtered": "total_filtered",
        "total_pages": "total_pages",
    }

    def __init__(self_, page_index: int, page_size: int, total_filtered: int, total_pages: int, **kwargs):
        """
        Pagination metadata for a unified hosts list response.

        :param page_index: The current page index (zero-based).
        :type page_index: int

        :param page_size: The number of hosts returned per page.
        :type page_size: int

        :param total_filtered: The total number of hosts matching the filter criteria.
        :type total_filtered: int

        :param total_pages: The total number of pages available.
        :type total_pages: int
        """
        super().__init__(kwargs)

        self_.page_index = page_index
        self_.page_size = page_size
        self_.total_filtered = total_filtered
        self_.total_pages = total_pages
