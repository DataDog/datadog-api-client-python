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
    UUID,
)


class TemporaryGrantRequestPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_cursor": (UUID,),
        }

    attribute_map = {
        "next_cursor": "next_cursor",
    }

    def __init__(self_, next_cursor: Union[UUID, UnsetType] = unset, **kwargs):
        """
        UUID cursor pagination. A full final page can return a cursor followed by an empty page.

        :param next_cursor: Use this UUID as page[cursor] to retrieve the next page. Omitted when the page is not full.
        :type next_cursor: UUID, optional
        """
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        super().__init__(kwargs)
