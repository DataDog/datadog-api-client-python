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
    from datadog_api_client.v2.model.automation_rule_create import AutomationRuleCreate


class AutomationRuleCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule_create import AutomationRuleCreate

        return {
            "data": (AutomationRuleCreate,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: AutomationRuleCreate, **kwargs):
        """
        Request payload for creating an automation rule.

        :param data: Data object for creating an automation rule.
        :type data: AutomationRuleCreate
        """
        super().__init__(kwargs)

        self_.data = data
