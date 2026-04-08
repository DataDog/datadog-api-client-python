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


class RuleAttributesRequest(ModelNormal):
    validations = {
        "level": {
            "inclusive_maximum": 3,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "enabled": (bool,),
            "level": (int,),
            "name": (str,),
            "owner": (str,),
            "scope_query": (str,),
            "scorecard_name": (str,),
        }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "level": "level",
        "name": "name",
        "owner": "owner",
        "scope_query": "scope_query",
        "scorecard_name": "scorecard_name",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        level: Union[int, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        owner: Union[str, UnsetType] = unset,
        scope_query: Union[str, UnsetType] = unset,
        scorecard_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a rule. Server-managed fields (created_at, modified_at, custom) are excluded.

        :param description: Explanation of the rule.
        :type description: str, optional

        :param enabled: If enabled, the rule is calculated as part of the score.
        :type enabled: bool, optional

        :param level: The maturity level of the rule (1, 2, or 3).
        :type level: int, optional

        :param name: Name of the rule.
        :type name: str, optional

        :param owner: Owner of the rule.
        :type owner: str, optional

        :param scope_query: A query to filter which entities this rule applies to.
        :type scope_query: str, optional

        :param scorecard_name: The scorecard name to which this rule must belong.
        :type scorecard_name: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if level is not unset:
            kwargs["level"] = level
        if name is not unset:
            kwargs["name"] = name
        if owner is not unset:
            kwargs["owner"] = owner
        if scope_query is not unset:
            kwargs["scope_query"] = scope_query
        if scorecard_name is not unset:
            kwargs["scorecard_name"] = scorecard_name
        super().__init__(kwargs)
