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


class DeploymentGatesListResponseMetaPage(ModelNormal):
    validations = {
        "size": {
            "inclusive_maximum": 1000,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "cursor": (str,),
            "next_cursor": (str,),
            "size": (int,),
        }

    attribute_map = {
        "cursor": "cursor",
        "next_cursor": "next_cursor",
        "size": "size",
    }

    def __init__(
        self_,
        cursor: Union[str, UnsetType] = unset,
        next_cursor: Union[str, UnsetType] = unset,
        size: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Pagination information for a list of deployment gates.

        :param cursor: The cursor used for the current page.
        :type cursor: str, optional

        :param next_cursor: The cursor to use to fetch the next page. This is absent when there are no more pages.
        :type next_cursor: str, optional

        :param size: The number of results per page.
        :type size: int, optional
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if next_cursor is not unset:
            kwargs["next_cursor"] = next_cursor
        if size is not unset:
            kwargs["size"] = size
        super().__init__(kwargs)
