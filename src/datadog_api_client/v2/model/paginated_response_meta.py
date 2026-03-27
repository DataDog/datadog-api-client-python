# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class PaginatedResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "limit": (int,),
            "offset": (int,),
            "total": (int,),
        }

    attribute_map = {
        "count": "count",
        "limit": "limit",
        "offset": "offset",
        "total": "total",
    }

    def __init__(self_, count: int, limit: int, offset: int, total: int, **kwargs):
        """
        Metadata for scores response.

        :param count: Number of entities in this response.
        :type count: int

        :param limit: Pagination limit.
        :type limit: int

        :param offset: Pagination offset.
        :type offset: int

        :param total: Total number of entities available.
        :type total: int
        """
        super().__init__(kwargs)

        self_.count = count
        self_.limit = limit
        self_.offset = offset
        self_.total = total
