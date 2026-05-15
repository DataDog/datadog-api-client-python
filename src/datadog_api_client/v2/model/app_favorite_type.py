# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppFavoriteType(ModelSimple):
    """
    The favorite resource type.

    :param value: If omitted defaults to "favorites". Must be one of ["favorites"].
    :type value: str
    """

    allowed_values = {
        "favorites",
    }
    FAVORITES: ClassVar["AppFavoriteType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppFavoriteType.FAVORITES = AppFavoriteType("favorites")
