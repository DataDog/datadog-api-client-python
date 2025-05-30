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


class KindAttributes(ModelNormal):
    validations = {
        "name": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "display_name": (str,),
            "name": (str,),
        }

    attribute_map = {
        "description": "description",
        "display_name": "displayName",
        "name": "name",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Kind attributes.

        :param description: Short description of the kind.
        :type description: str, optional

        :param display_name: User friendly name of the kind.
        :type display_name: str, optional

        :param name: The kind name.
        :type name: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
