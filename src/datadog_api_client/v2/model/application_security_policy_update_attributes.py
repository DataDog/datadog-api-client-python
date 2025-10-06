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
    from datadog_api_client.v2.model.application_security_policy_rule_override import (
        ApplicationSecurityPolicyRuleOverride,
    )
    from datadog_api_client.v2.model.application_security_policy_scope import ApplicationSecurityPolicyScope


class ApplicationSecurityPolicyUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_policy_rule_override import (
            ApplicationSecurityPolicyRuleOverride,
        )
        from datadog_api_client.v2.model.application_security_policy_scope import ApplicationSecurityPolicyScope

        return {
            "description": (str,),
            "is_default": (bool,),
            "name": (str,),
            "protection_presets": ([str],),
            "rules": ([ApplicationSecurityPolicyRuleOverride],),
            "scope": ([ApplicationSecurityPolicyScope],),
            "version": (int,),
        }

    attribute_map = {
        "description": "description",
        "is_default": "isDefault",
        "name": "name",
        "protection_presets": "protectionPresets",
        "rules": "rules",
        "scope": "scope",
        "version": "version",
    }

    def __init__(
        self_,
        description: str,
        is_default: bool,
        name: str,
        protection_presets: List[str],
        rules: List[ApplicationSecurityPolicyRuleOverride],
        scope: List[ApplicationSecurityPolicyScope],
        **kwargs,
    ):
        """
        Update a WAF policy.

        :param description: Description of the WAF policy.
        :type description: str

        :param is_default: Make this policy the default policy. The default policy is applied to every services not specifically added to another policy.
        :type is_default: bool

        :param name: The Name of the WAF policy.
        :type name: str

        :param protection_presets: Presets enabled on this policy.
        :type protection_presets: [str]

        :param rules: Rule overrides applied by the policy.
        :type rules: [ApplicationSecurityPolicyRuleOverride]

        :param scope: The scope of the WAF policy.
        :type scope: [ApplicationSecurityPolicyScope]

        :param version: Version of the WAF ruleset maintained by Datadog used by this policy. 0 is the default value.
        :type version: int
        """
        super().__init__(kwargs)
        version = kwargs.get("version", 0)

        self_.description = description
        self_.is_default = is_default
        self_.name = name
        self_.protection_presets = protection_presets
        self_.rules = rules
        self_.scope = scope
        self_.version = version
