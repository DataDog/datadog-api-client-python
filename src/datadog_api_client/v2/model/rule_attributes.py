# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class RuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "created_at": (datetime,),
            "custom": (bool,),
            "description": (str,),
            "enabled": (bool,),
            "modified_at": (datetime,),
            "name": (str,),
            "owner": (str,),
            "scorecard_name": (str,),
        }

    attribute_map = {
        "category": "category",
        "created_at": "created_at",
        "custom": "custom",
        "description": "description",
        "enabled": "enabled",
        "modified_at": "modified_at",
        "name": "name",
        "owner": "owner",
        "scorecard_name": "scorecard_name",
    }

    def __init__(
        self_,
        category: Union[str, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        custom: Union[bool, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        owner: Union[str, UnsetType] = unset,
        scorecard_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details of a rule.

        :param category: The scorecard name to which this rule must belong. **Deprecated**.
        :type category: str, optional

        :param created_at: Creation time of the rule outcome.
        :type created_at: datetime, optional

        :param custom: Defines if the rule is a custom rule.
        :type custom: bool, optional

        :param description: Explanation of the rule.
        :type description: str, optional

        :param enabled: If enabled, the rule is calculated as part of the score.
        :type enabled: bool, optional

        :param modified_at: Time of the last rule outcome modification.
        :type modified_at: datetime, optional

        :param name: Name of the rule.
        :type name: str, optional

        :param owner: Owner of the rule.
        :type owner: str, optional

        :param scorecard_name: The scorecard name to which this rule must belong.
        :type scorecard_name: str, optional
        """
        if category is not unset:
            kwargs["category"] = category
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if custom is not unset:
            kwargs["custom"] = custom
        if description is not unset:
            kwargs["description"] = description
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if name is not unset:
            kwargs["name"] = name
        if owner is not unset:
            kwargs["owner"] = owner
        if scorecard_name is not unset:
            kwargs["scorecard_name"] = scorecard_name
        super().__init__(kwargs)
