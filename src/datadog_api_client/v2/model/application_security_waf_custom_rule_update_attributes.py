# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_security_waf_custom_rule_action import (
        ApplicationSecurityWafCustomRuleAction,
    )
    from datadog_api_client.v2.model.application_security_waf_custom_rule_condition import (
        ApplicationSecurityWafCustomRuleCondition,
    )
    from datadog_api_client.v2.model.application_security_waf_custom_rule_scope import (
        ApplicationSecurityWafCustomRuleScope,
    )
    from datadog_api_client.v2.model.application_security_waf_custom_rule_tags import (
        ApplicationSecurityWafCustomRuleTags,
    )


class ApplicationSecurityWafCustomRuleUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_custom_rule_action import (
            ApplicationSecurityWafCustomRuleAction,
        )
        from datadog_api_client.v2.model.application_security_waf_custom_rule_condition import (
            ApplicationSecurityWafCustomRuleCondition,
        )
        from datadog_api_client.v2.model.application_security_waf_custom_rule_scope import (
            ApplicationSecurityWafCustomRuleScope,
        )
        from datadog_api_client.v2.model.application_security_waf_custom_rule_tags import (
            ApplicationSecurityWafCustomRuleTags,
        )

        return {
            "action": (ApplicationSecurityWafCustomRuleAction,),
            "blocking": (bool,),
            "conditions": ([ApplicationSecurityWafCustomRuleCondition],),
            "enabled": (bool,),
            "name": (str,),
            "path_glob": (str,),
            "scope": ([ApplicationSecurityWafCustomRuleScope],),
            "tags": (ApplicationSecurityWafCustomRuleTags,),
        }

    attribute_map = {
        "action": "action",
        "blocking": "blocking",
        "conditions": "conditions",
        "enabled": "enabled",
        "name": "name",
        "path_glob": "path_glob",
        "scope": "scope",
        "tags": "tags",
    }

    def __init__(
        self_,
        blocking: bool,
        conditions: List[ApplicationSecurityWafCustomRuleCondition],
        enabled: bool,
        name: str,
        tags: ApplicationSecurityWafCustomRuleTags,
        action: Union[ApplicationSecurityWafCustomRuleAction, UnsetType] = unset,
        path_glob: Union[str, UnsetType] = unset,
        scope: Union[List[ApplicationSecurityWafCustomRuleScope], UnsetType] = unset,
        **kwargs,
    ):
        """
        Update a WAF custom rule.

        :param action: The definition of ``ApplicationSecurityWafCustomRuleAction`` object.
        :type action: ApplicationSecurityWafCustomRuleAction, optional

        :param blocking: Indicates whether the WAF custom rule will block the request.
        :type blocking: bool

        :param conditions: Conditions for which the WAF Custom Rule will triggers, all conditions needs to match in order for the WAF
            rule to trigger.
        :type conditions: [ApplicationSecurityWafCustomRuleCondition]

        :param enabled: Indicates whether the WAF custom rule is enabled.
        :type enabled: bool

        :param name: The Name of the WAF custom rule.
        :type name: str

        :param path_glob: The path glob for the WAF custom rule.
        :type path_glob: str, optional

        :param scope: The scope of the WAF custom rule.
        :type scope: [ApplicationSecurityWafCustomRuleScope], optional

        :param tags: Tags associated with the WAF Custom Rule. The concatenation of category and type will form the security
            activity field associated with the traces.
        :type tags: ApplicationSecurityWafCustomRuleTags
        """
        if action is not unset:
            kwargs["action"] = action
        if path_glob is not unset:
            kwargs["path_glob"] = path_glob
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)

        self_.blocking = blocking
        self_.conditions = conditions
        self_.enabled = enabled
        self_.name = name
        self_.tags = tags
