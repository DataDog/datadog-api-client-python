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


class ListInvestigationsResponseLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first": (str,),
            "last": (str, none_type),
            "next": (str,),
            "prev": (str, none_type),
            "self": (str,),
        }

    attribute_map = {
        "first": "first",
        "last": "last",
        "next": "next",
        "prev": "prev",
        "self": "self",
    }

    def __init__(
        self_,
        first: str,
        next: str,
        self: str,
        last: Union[str, none_type, UnsetType] = unset,
        prev: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination links for the list investigations response.

        :param first: Link to the first page.
        :type first: str

        :param last: Link to the last page.
        :type last: str, none_type, optional

        :param next: Link to the next page.
        :type next: str

        :param prev: Link to the previous page.
        :type prev: str, none_type, optional

        :param self: Link to the current page.
        :type self: str
        """
        if last is not unset:
            kwargs["last"] = last
        if prev is not unset:
            kwargs["prev"] = prev
        super().__init__(kwargs)

        self_.first = first
        self_.next = next
        self_.self = self
