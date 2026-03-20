# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentUserDefinedFieldListMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "page_offset": (int,),
            "total": (int,),
        }

    attribute_map = {
        "page_offset": "page_offset",
        "total": "total",
    }

    def __init__(self_, page_offset: int, total: int, **kwargs):
        """
        Pagination metadata for the user-defined field list response.

        :param page_offset: The offset of the current page.
        :type page_offset: int

        :param total: The total number of items in the current page.
        :type total: int
        """
        super().__init__(kwargs)

        self_.page_offset = page_offset
        self_.total = total
