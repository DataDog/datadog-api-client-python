# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rule_based_view_compliance_framework import RuleBasedViewComplianceFramework
    from datadog_api_client.v2.model.rule_based_view_rule_stats import RuleBasedViewRuleStats
    from datadog_api_client.v2.model.rule_based_view_rule_category import RuleBasedViewRuleCategory


class RuleBasedViewRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_based_view_compliance_framework import RuleBasedViewComplianceFramework
        from datadog_api_client.v2.model.rule_based_view_rule_stats import RuleBasedViewRuleStats
        from datadog_api_client.v2.model.rule_based_view_rule_category import RuleBasedViewRuleCategory

        return {
            "compliance_frameworks": ([RuleBasedViewComplianceFramework],),
            "enabled": (bool,),
            "id": (str,),
            "name": (str,),
            "resource_attributes": ([str],),
            "resource_category": (str,),
            "resource_type": (str,),
            "stats": (RuleBasedViewRuleStats,),
            "status": (str,),
            "tags": ([str],),
            "type": (RuleBasedViewRuleCategory,),
        }

    attribute_map = {
        "compliance_frameworks": "compliance_frameworks",
        "enabled": "enabled",
        "id": "id",
        "name": "name",
        "resource_attributes": "resourceAttributes",
        "resource_category": "resourceCategory",
        "resource_type": "resourceType",
        "stats": "stats",
        "status": "status",
        "tags": "tags",
        "type": "type",
    }

    def __init__(
        self_,
        compliance_frameworks: List[RuleBasedViewComplianceFramework],
        enabled: bool,
        id: str,
        name: str,
        resource_attributes: List[str],
        resource_category: str,
        resource_type: str,
        stats: RuleBasedViewRuleStats,
        status: str,
        tags: List[str],
        type: RuleBasedViewRuleCategory,
        **kwargs,
    ):
        """
        A compliance rule along with its evaluation statistics and framework mappings.

        :param compliance_frameworks: List of compliance framework mappings associated with the rule.
        :type compliance_frameworks: [RuleBasedViewComplianceFramework]

        :param enabled: Whether the rule is enabled.
        :type enabled: bool

        :param id: Unique identifier of the rule.
        :type id: str

        :param name: Human-readable name of the rule.
        :type name: str

        :param resource_attributes: List of resource attribute names exposed by the rule.
        :type resource_attributes: [str]

        :param resource_category: Resource category targeted by the rule.
        :type resource_category: str

        :param resource_type: Resource type targeted by the rule.
        :type resource_type: str

        :param stats: Counts of findings for the rule, grouped by their evaluation status.
        :type stats: RuleBasedViewRuleStats

        :param status: Severity associated with the rule (for example, ``info`` , ``low`` , ``medium`` , ``high`` , or ``critical`` ).
        :type status: str

        :param tags: List of tags attached to the rule.
        :type tags: [str]

        :param type: The category of the security rule.
        :type type: RuleBasedViewRuleCategory
        """
        super().__init__(kwargs)

        self_.compliance_frameworks = compliance_frameworks
        self_.enabled = enabled
        self_.id = id
        self_.name = name
        self_.resource_attributes = resource_attributes
        self_.resource_category = resource_category
        self_.resource_type = resource_type
        self_.stats = stats
        self_.status = status
        self_.tags = tags
        self_.type = type
