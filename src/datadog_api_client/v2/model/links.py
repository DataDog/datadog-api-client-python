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


class Links(ModelNormal):
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
        first: str,
        last: str,
        self: str,
        next: Union[str, UnsetType] = unset,
        previous: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The JSON:API links related to pagination.

        :param first: First page link.
        :type first: str

        :param last: Last page link.
        :type last: str

        :param next: Next page link.
        :type next: str, optional

        :param previous: Previous page link.
        :type previous: str, optional

        :param self: Request link.
        :type self: str
        """
        if next is not unset:
            kwargs["next"] = next
        if previous is not unset:
            kwargs["previous"] = previous
        super().__init__(kwargs)

        self_.first = first
        self_.last = last
        self_.self = self
