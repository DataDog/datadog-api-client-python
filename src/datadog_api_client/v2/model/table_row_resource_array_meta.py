# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TableRowResourceArrayMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "found_count": (int,),
            "not_found": ([str],),
            "requested_count": (int,),
        }

    attribute_map = {
        "found_count": "found_count",
        "not_found": "not_found",
        "requested_count": "requested_count",
    }

    def __init__(self_, found_count: int, not_found: List[str], requested_count: int, **kwargs):
        """
        Metadata about the rows requested, including which ones were not found.

        :param found_count: Number of requested rows that were found and returned in ``data``.
        :type found_count: int

        :param not_found: Row IDs from the request that do not exist in the reference table. Empty when every requested row was found.
        :type not_found: [str]

        :param requested_count: Number of row IDs supplied in the ``row_id`` query parameter.
        :type requested_count: int
        """
        super().__init__(kwargs)

        self_.found_count = found_count
        self_.not_found = not_found
        self_.requested_count = requested_count
