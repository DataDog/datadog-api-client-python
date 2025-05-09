# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CloudWorkloadSecurityAgentRuleCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "description": (str,),
            "enabled": (bool,),
            "expression": (str,),
            "filters": ([str],),
            "name": (str,),
            "policy_id": (str,),
            "product_tags": ([str],),
        }

    attribute_map = {
        "description": "description",
        "enabled": "enabled",
        "expression": "expression",
        "filters": "filters",
        "name": "name",
        "policy_id": "policy_id",
        "product_tags": "product_tags",
    }

    def __init__(
        self_,
        expression: str,
        name: str,
        description: Union[str, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        filters: Union[List[str], UnsetType] = unset,
        policy_id: Union[str, UnsetType] = unset,
        product_tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Create a new Cloud Workload Security Agent rule.

        :param description: The description of the Agent rule.
        :type description: str, optional

        :param enabled: Whether the Agent rule is enabled
        :type enabled: bool, optional

        :param expression: The SECL expression of the Agent rule.
        :type expression: str

        :param filters: The platforms the Agent rule is supported on
        :type filters: [str], optional

        :param name: The name of the Agent rule.
        :type name: str

        :param policy_id: The ID of the policy where the Agent rule is saved
        :type policy_id: str, optional

        :param product_tags: The list of product tags associated with the rule
        :type product_tags: [str], optional
        """
        if description is not unset:
            kwargs["description"] = description
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if filters is not unset:
            kwargs["filters"] = filters
        if policy_id is not unset:
            kwargs["policy_id"] = policy_id
        if product_tags is not unset:
            kwargs["product_tags"] = product_tags
        super().__init__(kwargs)

        self_.expression = expression
        self_.name = name
