# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_context_page import EntityContextPage


class EntityContextResponseMeta(ModelNormal):
    validations = {
        "total_count": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_context_page import EntityContextPage

        return {
            "page": (EntityContextPage,),
            "total_count": (int,),
        }

    attribute_map = {
        "page": "page",
        "total_count": "total_count",
    }

    def __init__(self_, page: EntityContextPage, total_count: int, **kwargs):
        """
        Metadata returned alongside the entity context response.

        :param page: Pagination metadata for the entity context response.
        :type page: EntityContextPage

        :param total_count: The total number of entities matching the query, irrespective of pagination.
        :type total_count: int
        """
        super().__init__(kwargs)

        self_.page = page
        self_.total_count = total_count
