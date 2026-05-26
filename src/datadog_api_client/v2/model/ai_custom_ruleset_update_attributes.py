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


class AiCustomRulesetUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "name": (str,),
            "short_description": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "short_description": "short_description",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        short_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating an AI custom ruleset.

        :param description: Base64-encoded full description of the ruleset.
        :type description: str, optional

        :param name: The ruleset name.
        :type name: str, optional

        :param short_description: Base64-encoded short description of the ruleset.
        :type short_description: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if short_description is not unset:
            kwargs["short_description"] = short_description
        super().__init__(kwargs)
