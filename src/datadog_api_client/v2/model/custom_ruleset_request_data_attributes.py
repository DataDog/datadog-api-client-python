# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_rule import CustomRule


class CustomRulesetRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule import CustomRule

        return {
            "description": (str,),
            "name": (str,),
            "rules": ([CustomRule], none_type),
            "short_description": (str,),
        }

    attribute_map = {
        "description": "description",
        "name": "name",
        "rules": "rules",
        "short_description": "short_description",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        rules: Union[List[CustomRule], none_type, UnsetType] = unset,
        short_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param description: Base64-encoded full description
        :type description: str, optional

        :param name: Ruleset name
        :type name: str, optional

        :param rules: Rules in the ruleset
        :type rules: [CustomRule], none_type, optional

        :param short_description: Base64-encoded short description
        :type short_description: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if rules is not unset:
            kwargs["rules"] = rules
        if short_description is not unset:
            kwargs["short_description"] = short_description
        super().__init__(kwargs)
