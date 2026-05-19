# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.automation_rule_create_attributes import AutomationRuleCreateAttributes
    from datadog_api_client.v2.model.case_automation_rule_resource_type import CaseAutomationRuleResourceType


class AutomationRuleUpdate(ModelNormal):
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

    def __init__(
        self_,
        type: CaseAutomationRuleResourceType,
        attributes: Union[AutomationRuleCreateAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for updating an automation rule.

        :param attributes: Attributes required to create an automation rule.
        :type attributes: AutomationRuleCreateAttributes, optional

        :param type: JSON:API resource type for case automation rules.
        :type type: CaseAutomationRuleResourceType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
