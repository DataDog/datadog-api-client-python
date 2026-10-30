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


class RUMOperationsListResponseLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first": (str,),
            "last": (str,),
            "next": (str,),
            "prev": (str,),
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
        first: Union[str, UnsetType] = unset,
        last: Union[str, UnsetType] = unset,
        next: Union[str, UnsetType] = unset,
        prev: Union[str, UnsetType] = unset,
        self: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination links for a list of RUM operations.

        :param first: Link to the first page.
        :type first: str, optional

        :param last: Link to the last page.
        :type last: str, optional

        :param next: Link to the next page.
        :type next: str, optional

        :param prev: Link to the previous page.
        :type prev: str, optional

        :param self: Link to the current page.
        :type self: str, optional
        """
        if first is not unset:
            kwargs["first"] = first
        if last is not unset:
            kwargs["last"] = last
        if next is not unset:
            kwargs["next"] = next
        if prev is not unset:
            kwargs["prev"] = prev
        if self is not unset:
            kwargs["self"] = self
        super().__init__(kwargs)
