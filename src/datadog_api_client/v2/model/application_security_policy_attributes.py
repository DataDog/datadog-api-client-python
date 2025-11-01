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
    from datadog_api_client.v2.model.application_security_policy_rule_override import (
        ApplicationSecurityPolicyRuleOverride,
    )
    from datadog_api_client.v2.model.application_security_policy_scope import ApplicationSecurityPolicyScope


class ApplicationSecurityPolicyAttributes(ModelNormal):
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
        name: str,
        is_default: Union[bool, UnsetType] = unset,
        protection_presets: Union[List[str], UnsetType] = unset,
        rules: Union[List[ApplicationSecurityPolicyRuleOverride], UnsetType] = unset,
        scope: Union[List[ApplicationSecurityPolicyScope], UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A WAF policy.

        :param description: Description of the WAF policy.
        :type description: str

        :param is_default: Make this policy the default policy. The default policy is applied to every services not specifically added to another policy.
        :type is_default: bool, optional

        :param name: The Name of the WAF policy.
        :type name: str

        :param protection_presets: Presets enabled on this policy.
        :type protection_presets: [str], optional

        :param rules: Rule overrides applied by the policy.
        :type rules: [ApplicationSecurityPolicyRuleOverride], optional

        :param scope: The scope of the WAF policy.
        :type scope: [ApplicationSecurityPolicyScope], optional

        :param version: Version of the WAF ruleset maintained by Datadog used by this policy. 0 is the default value.
        :type version: int, optional
        """
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if protection_presets is not unset:
            kwargs["protection_presets"] = protection_presets
        if rules is not unset:
            kwargs["rules"] = rules
        if scope is not unset:
            kwargs["scope"] = scope
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.description = description
        self_.name = name
