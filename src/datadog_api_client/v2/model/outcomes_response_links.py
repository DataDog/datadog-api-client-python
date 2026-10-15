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


class OutcomesResponseLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "first": (str,),
            "last": (str,),
            "next": (str,),
            "previous": (str,),
            "self": (str,),
        }

    attribute_map = {
        "first": "first",
        "last": "last",
        "next": "next",
        "previous": "previous",
        "self": "self",
    }

    def __init__(
        self_,
        first: Union[str, UnsetType] = unset,
        last: Union[str, UnsetType] = unset,
        next: Union[str, UnsetType] = unset,
        previous: Union[str, UnsetType] = unset,
        self: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination links for rule outcomes.

        :param first: Link for the first set of results.
        :type first: str, optional

        :param last: Link for the last set of results.
        :type last: str, optional

        :param next: Link for the next set of results.
        :type next: str, optional

        :param previous: Link for the previous set of results.
        :type previous: str, optional

        :param self: Link for the current set of results.
        :type self: str, optional
        """
        if first is not unset:
            kwargs["first"] = first
        if last is not unset:
            kwargs["last"] = last
        if next is not unset:
            kwargs["next"] = next
        if previous is not unset:
            kwargs["previous"] = previous
        if self is not unset:
            kwargs["self"] = self
        super().__init__(kwargs)
