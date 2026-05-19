# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.automation_rule import AutomationRule


class AutomationRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule import AutomationRule

        return {
            "data": (AutomationRule,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AutomationRule, **kwargs):
        """
        Response containing a single automation rule.

        :param data: An automation rule that executes an action (such as running a Datadog workflow or assigning an AI agent) when a specified case event occurs within a project.
        :type data: AutomationRule
        """
        super().__init__(kwargs)

        self_.data = data
