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


class ExperimentsOffsetLinks(ModelNormal):
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
        Links for navigating a paginated result set.

        :param first: URL of the first page of results.
        :type first: str, optional

        :param last: URL of the last page of results.
        :type last: str, optional

        :param next: URL of the next page of results.
        :type next: str, optional

        :param prev: URL of the previous page of results.
        :type prev: str, optional

        :param self: URL of the current page of results.
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
