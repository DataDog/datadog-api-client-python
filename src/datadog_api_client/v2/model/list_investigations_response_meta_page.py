# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ListInvestigationsResponseMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "limit": (int,),
            "offset": (int,),
            "total": (int,),
        }

    attribute_map = {
        "limit": "limit",
        "offset": "offset",
        "total": "total",
    }

    def __init__(self_, limit: int, offset: int, total: int, **kwargs):
        """
        Pagination metadata.

        :param limit: Maximum number of results per page.
        :type limit: int

        :param offset: Offset of the current page.
        :type offset: int

        :param total: Total number of investigations.
        :type total: int
        """
        super().__init__(kwargs)

        self_.limit = limit
        self_.offset = offset
        self_.total = total
