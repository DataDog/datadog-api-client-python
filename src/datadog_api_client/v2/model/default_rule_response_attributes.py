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


class DefaultRuleResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "level": (int,),
            "name": (str,),
            "scope_required": (str,),
            "scorecard_description": (str,),
            "scorecard_name": (str,),
        }

    attribute_map = {
        "description": "description",
        "level": "level",
        "name": "name",
        "scope_required": "scope_required",
        "scorecard_description": "scorecard_description",
        "scorecard_name": "scorecard_name",
    }

    def __init__(
        self_,
        name: str,
        scorecard_name: str,
        description: Union[str, UnsetType] = unset,
        level: Union[int, UnsetType] = unset,
        scope_required: Union[str, UnsetType] = unset,
        scorecard_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Default rule attributes.

        :param description: The description of the default rule.
        :type description: str, optional

        :param level: The maturity level of the rule.
        :type level: int, optional

        :param name: The name of the default rule.
        :type name: str

        :param scope_required: Required scope for the rule.
        :type scope_required: str, optional

        :param scorecard_description: The description of the scorecard.
        :type scorecard_description: str, optional

        :param scorecard_name: The scorecard this rule belongs to.
        :type scorecard_name: str
        """
        if description is not unset:
            kwargs["description"] = description
        if level is not unset:
            kwargs["level"] = level
        if scope_required is not unset:
            kwargs["scope_required"] = scope_required
        if scorecard_description is not unset:
            kwargs["scorecard_description"] = scorecard_description
        super().__init__(kwargs)

        self_.name = name
        self_.scorecard_name = scorecard_name
