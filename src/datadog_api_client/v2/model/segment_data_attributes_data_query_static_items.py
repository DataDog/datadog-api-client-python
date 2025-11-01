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


class SegmentDataAttributesDataQueryStaticItems(ModelNormal):
    validations = {
        "user_count": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "name": (str,),
            "user_count": (int,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "user_count": "user_count",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        user_count: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param id:
        :type id: str, optional

        :param name:
        :type name: str, optional

        :param user_count:
        :type user_count: int, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if user_count is not unset:
            kwargs["user_count"] = user_count
        super().__init__(kwargs)
