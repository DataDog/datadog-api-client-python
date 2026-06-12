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


class GlobalOrgsLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next": (str, none_type),
            "prev": (str, none_type),
            "self": (str,),
        }

    attribute_map = {
        "next": "next",
        "prev": "prev",
        "self": "self",
    }

    def __init__(
        self_,
        next: Union[str, none_type, UnsetType] = unset,
        prev: Union[str, none_type, UnsetType] = unset,
        self: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination links.

        :param next: Link to the next page.
        :type next: str, none_type, optional

        :param prev: Link to the previous page.
        :type prev: str, none_type, optional

        :param self: Link to the current page.
        :type self: str, optional
        """
        if next is not unset:
            kwargs["next"] = next
        if prev is not unset:
            kwargs["prev"] = prev
        if self is not unset:
            kwargs["self"] = self
        super().__init__(kwargs)
