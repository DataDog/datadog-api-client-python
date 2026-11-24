# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityAgentOutreachRuleUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "is_enabled": (bool,),
            "rule_id": (str,),
        }

    attribute_map = {
        "is_enabled": "is_enabled",
        "rule_id": "rule_id",
    }

    def __init__(self_, is_enabled: bool, rule_id: str, **kwargs):
        """
        The outreach automation state to set for one detection rule.

        :param is_enabled: Whether the rule auto-sends automated interviews in ``automated`` mode. Required.
        :type is_enabled: bool

        :param rule_id: ID of the detection rule. Must be non-empty.
        :type rule_id: str
        """
        super().__init__(kwargs)

        self_.is_enabled = is_enabled
        self_.rule_id = rule_id
