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
    from datadog_api_client.v2.model.automation_rule_create_attributes import AutomationRuleCreateAttributes
    from datadog_api_client.v2.model.case_automation_rule_resource_type import CaseAutomationRuleResourceType


class AutomationRuleCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule_create_attributes import AutomationRuleCreateAttributes
        from datadog_api_client.v2.model.case_automation_rule_resource_type import CaseAutomationRuleResourceType

        return {
            "attributes": (AutomationRuleCreateAttributes,),
            "type": (CaseAutomationRuleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: AutomationRuleCreateAttributes, type: CaseAutomationRuleResourceType, **kwargs):
        """
        Data object for creating an automation rule.

        :param attributes: Attributes required to create an automation rule.
        :type attributes: AutomationRuleCreateAttributes

        :param type: JSON:API resource type for case automation rules.
        :type type: CaseAutomationRuleResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
