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


class ListRowsResponseLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first": (str,),
            "next": (str,),
            "self": (str,),
        }

    attribute_map = {
        "first": "first",
        "next": "next",
        "self": "self",
    }

    def __init__(self_, first: str, self: str, next: Union[str, UnsetType] = unset, **kwargs):
        """
        Pagination links for the list rows response.

        :param first: Link to the first page of results.
        :type first: str

        :param next: Link to the next page of results. Only present when more rows are available.
        :type next: str, optional

        :param self: Link to the current page of results.
        :type self: str
        """
        if next is not unset:
            kwargs["next"] = next
        super().__init__(kwargs)

        self_.first = first
        self_.self = self
