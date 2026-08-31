# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class UsageQuotasResponseMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_cursor": (str,),
        }

    attribute_map = {
        "next_cursor": "next_cursor",
    }

    def __init__(self_, next_cursor: Union[str, UnsetType] = unset, **kwargs):
        """
        Cursor pagination fields for a usage quota list response.

        :param next_cursor: An opaque cursor for retrieving the next page. Omitted when there are no more results.
        :type next_cursor: str, optional
        """
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)
