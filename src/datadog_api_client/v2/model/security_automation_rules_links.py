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


class SecurityAutomationRulesLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first": (str,),
            "last": (str,),
            "next": (str,),
            "prev": (str,),
        }

    attribute_map = {
        "first": "first",
        "last": "last",
        "next": "next",
        "prev": "prev",
    }

    def __init__(
        self_, first: str, last: str, next: Union[str, UnsetType] = unset, prev: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Pagination links for the list of automation rules.

        :param first: Link to the first page of results.
        :type first: str

        :param last: Link to the last page of results.
        :type last: str

        :param next: Link to the next page of results.
        :type next: str, optional

        :param prev: Link to the previous page of results.
        :type prev: str, optional
        """
        if next is not unset:
            kwargs["next"] = next
        if prev is not unset:
            kwargs["prev"] = prev
        super().__init__(kwargs)

        self_.first = first
        self_.last = last
