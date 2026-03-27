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


class WidgetSearchMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_by_anyone_total": (int,),
            "created_by_you_total": (int,),
            "favorited_by_you_total": (int,),
            "filtered_total": (int,),
        }

    attribute_map = {
        "created_by_anyone_total": "created_by_anyone_total",
        "created_by_you_total": "created_by_you_total",
        "favorited_by_you_total": "favorited_by_you_total",
        "filtered_total": "filtered_total",
    }

    def __init__(
        self_,
        created_by_anyone_total: Union[int, UnsetType] = unset,
        created_by_you_total: Union[int, UnsetType] = unset,
        favorited_by_you_total: Union[int, UnsetType] = unset,
        filtered_total: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata about the search results.

        :param created_by_anyone_total: Total number of widgets created by anyone.
        :type created_by_anyone_total: int, optional

        :param created_by_you_total: Total number of widgets created by the current user.
        :type created_by_you_total: int, optional

        :param favorited_by_you_total: Total number of widgets favorited by the current user.
        :type favorited_by_you_total: int, optional

        :param filtered_total: Total number of widgets matching the current filter criteria.
        :type filtered_total: int, optional
        """
        if created_by_anyone_total is not unset:
            kwargs["created_by_anyone_total"] = created_by_anyone_total
        if created_by_you_total is not unset:
            kwargs["created_by_you_total"] = created_by_you_total
        if favorited_by_you_total is not unset:
            kwargs["favorited_by_you_total"] = favorited_by_you_total
        if filtered_total is not unset:
            kwargs["filtered_total"] = filtered_total
        super().__init__(kwargs)
