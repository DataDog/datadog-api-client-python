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
    from datadog_api_client.v2.model.ownership_history_item import OwnershipHistoryItem
    from datadog_api_client.v2.model.ownership_history_pagination import OwnershipHistoryPagination


class OwnershipHistoryAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_history_item import OwnershipHistoryItem
        from datadog_api_client.v2.model.ownership_history_pagination import OwnershipHistoryPagination

        return {
            "items": ([OwnershipHistoryItem],),
            "pagination": (OwnershipHistoryPagination,),
        }

    attribute_map = {
        "items": "items",
        "pagination": "pagination",
    }

    def __init__(self_, items: List[OwnershipHistoryItem], pagination: OwnershipHistoryPagination, **kwargs):
        """
        The attributes of an ownership history response.

        :param items: The list of history entries returned for this page.
        :type items: [OwnershipHistoryItem]

        :param pagination: Cursor-based pagination metadata for the history response.
        :type pagination: OwnershipHistoryPagination
        """
        super().__init__(kwargs)

        self_.items = items
        self_.pagination = pagination
