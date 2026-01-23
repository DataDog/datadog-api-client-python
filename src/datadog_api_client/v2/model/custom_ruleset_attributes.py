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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_rule import CustomRule


class CustomRulesetAttributes(ModelNormal):
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
        created_at: datetime,
        created_by: str,
        description: str,
        name: str,
        rules: Union[List[CustomRule], none_type],
        short_description: str,
        **kwargs,
    ):
        """


        :param created_at: Creation timestamp
        :type created_at: datetime

        :param created_by: Creator identifier
        :type created_by: str

        :param description: Base64-encoded full description
        :type description: str

        :param name: Ruleset name
        :type name: str

        :param rules: Rules in the ruleset
        :type rules: [CustomRule], none_type

        :param short_description: Base64-encoded short description
        :type short_description: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.description = description
        self_.name = name
        self_.rules = rules
        self_.short_description = short_description
