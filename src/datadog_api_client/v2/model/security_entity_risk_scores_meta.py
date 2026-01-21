# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityEntityRiskScoresMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "page_number": (int,),
            "page_size": (int,),
            "query_id": (str,),
            "total_row_count": (int,),
        }

    attribute_map = {
        "page_number": "pageNumber",
        "page_size": "pageSize",
        "query_id": "queryId",
        "total_row_count": "totalRowCount",
    }

    def __init__(self_, page_number: int, page_size: int, query_id: str, total_row_count: int, **kwargs):
        """
        Metadata for pagination

        :param page_number: Current page number (1-indexed)
        :type page_number: int

        :param page_size: Number of items per page
        :type page_size: int

        :param query_id: Query ID for pagination consistency
        :type query_id: str

        :param total_row_count: Total number of entities matching the query
        :type total_row_count: int
        """
        super().__init__(kwargs)

        self_.page_number = page_number
        self_.page_size = page_size
        self_.query_id = query_id
        self_.total_row_count = total_row_count
