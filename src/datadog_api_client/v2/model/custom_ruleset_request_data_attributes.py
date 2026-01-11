# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
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
            "created_at": (datetime,),
            "created_by": (str,),
            "description": (str,),
            "name": (str,),
            "rules": ([CustomRule], none_type),
            "short_description": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "name": "name",
        "rules": "rules",
        "short_description": "short_description",
    }

    def __init__(
        self_,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        rules: Union[List[CustomRule], none_type, UnsetType] = unset,
        short_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param created_at: Creation timestamp (auto-generated on server)
        :type created_at: datetime, optional

        :param created_by: Creator identifier (auto-generated on server)
        :type created_by: str, optional

        :param description: Base64-encoded full description
        :type description: str, optional

        :param name: Ruleset name
        :type name: str, optional

        :param rules: Rules in the ruleset
        :type rules: [CustomRule], none_type, optional

        :param short_description: Base64-encoded short description
        :type short_description: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if rules is not unset:
            kwargs["rules"] = rules
        if short_description is not unset:
            kwargs["short_description"] = short_description
        super().__init__(kwargs)
