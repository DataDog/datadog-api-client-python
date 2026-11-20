# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RemediationGroupsPageMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "number": (int,),
            "size": (int,),
            "total_filtered_count": (int,),
        }

    attribute_map = {
        "number": "number",
        "size": "size",
        "total_filtered_count": "total_filtered_count",
    }

    def __init__(self_, number: int, size: int, total_filtered_count: int, **kwargs):
        """
        Pagination of the search.

        :param number: Page number, starting at 1.
        :type number: int

        :param size: Page size.
        :type size: int

        :param total_filtered_count: Number of groups that match the search across all pages.
        :type total_filtered_count: int
        """
        super().__init__(kwargs)

        self_.number = number
        self_.size = size
        self_.total_filtered_count = total_filtered_count
