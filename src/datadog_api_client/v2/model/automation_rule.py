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
    from datadog_api_client.v2.model.automation_rule_attributes import AutomationRuleAttributes
    from datadog_api_client.v2.model.automation_rule_relationships import AutomationRuleRelationships
    from datadog_api_client.v2.model.case_automation_rule_resource_type import CaseAutomationRuleResourceType


class AutomationRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.automation_rule_attributes import AutomationRuleAttributes
        from datadog_api_client.v2.model.automation_rule_relationships import AutomationRuleRelationships
        from datadog_api_client.v2.model.case_automation_rule_resource_type import CaseAutomationRuleResourceType

        return {
            "attributes": (AutomationRuleAttributes,),
            "id": (str,),
            "relationships": (AutomationRuleRelationships,),
            "type": (CaseAutomationRuleResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AutomationRuleAttributes,
        id: str,
        type: CaseAutomationRuleResourceType,
        relationships: Union[AutomationRuleRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        An automation rule that executes an action (such as running a Datadog workflow or assigning an AI agent) when a specified case event occurs within a project.

        :param attributes: Core attributes of an automation rule, including its name, trigger condition, action to execute, and current state.
        :type attributes: AutomationRuleAttributes

        :param id: Automation rule identifier.
        :type id: str

        :param relationships: Related resources for the automation rule, including the users who created and last modified it.
        :type relationships: AutomationRuleRelationships, optional

        :param type: JSON:API resource type for case automation rules.
        :type type: CaseAutomationRuleResourceType
        """
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
