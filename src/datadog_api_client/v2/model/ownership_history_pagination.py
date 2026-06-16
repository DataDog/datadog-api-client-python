# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class OwnershipHistoryPagination(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "has_more": (bool,),
            "next_cursor": (str, none_type),
        }

    attribute_map = {
        "has_more": "has_more",
        "next_cursor": "next_cursor",
    }

    def __init__(self_, has_more: bool, next_cursor: Union[str, none_type, UnsetType] = unset, **kwargs):
        """
        Cursor-based pagination metadata for the history response.

        :param has_more: Whether more history entries are available beyond this page.
        :type has_more: bool

        :param next_cursor: An opaque, base64-encoded cursor token. Pass it as the ``cursor`` query parameter to retrieve the next page. Absent or ``null`` when there are no further pages.
        :type next_cursor: str, none_type, optional
        """
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)

        self_.has_more = has_more
