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


class ListEntityCatalogResponseLinks(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next": (str,),
            "previous": (str,),
            "self": (str,),
        }

    attribute_map = {
        "next": "next",
        "previous": "previous",
        "self": "self",
    }

    def __init__(
        self_,
        next: Union[str, UnsetType] = unset,
        previous: Union[str, UnsetType] = unset,
        self: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        List entity response links.

        :param next: next link.
        :type next: str, optional

        :param previous: previous link.
        :type previous: str, optional

        :param self: current link.
        :type self: str, optional
        """
        if next is not unset:
            kwargs["next"] = next
        if previous is not unset:
            kwargs["previous"] = previous
        if self is not unset:
            kwargs["self"] = self
        super().__init__(kwargs)
