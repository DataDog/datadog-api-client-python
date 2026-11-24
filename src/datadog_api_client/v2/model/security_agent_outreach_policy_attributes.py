# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_agent_outreach_mode import SecurityAgentOutreachMode
    from datadog_api_client.v2.model.security_agent_outreach_rule import SecurityAgentOutreachRule


class SecurityAgentOutreachPolicyAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_agent_outreach_mode import SecurityAgentOutreachMode
        from datadog_api_client.v2.model.security_agent_outreach_rule import SecurityAgentOutreachRule

        return {
            "allowed_domains": ([str], none_type),
            "mode": (SecurityAgentOutreachMode,),
            "rules": ([SecurityAgentOutreachRule], none_type),
            "suggested_domains": ([str], none_type),
        }

    attribute_map = {
        "allowed_domains": "allowed_domains",
        "mode": "mode",
        "rules": "rules",
        "suggested_domains": "suggested_domains",
    }

    def __init__(
        self_,
        mode: SecurityAgentOutreachMode,
        allowed_domains: Union[List[str], none_type, UnsetType] = unset,
        rules: Union[List[SecurityAgentOutreachRule], none_type, UnsetType] = unset,
        suggested_domains: Union[List[str], none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the organization's outreach policy.

        :param allowed_domains: Email domains user outreach can be sent to, at most 20. ``null`` when none are allowed.
        :type allowed_domains: [str], none_type, optional

        :param mode: The organization's outreach mode. ``off`` disables user outreach. ``manual`` only sends outreach an analyst
            triggers. ``automated`` auto-sends automated interviews for rules with outreach enabled, to users whose email
            domain is allowed.
        :type mode: SecurityAgentOutreachMode

        :param rules: The stored per-rule automation state, including rules that are explicitly disabled. ``null`` when the
            organization has no stored rule state.
        :type rules: [SecurityAgentOutreachRule], none_type, optional

        :param suggested_domains: Domains the caller could allow next: their own email domain when it is not allowed yet and is not a
            consumer mailbox provider. Read-only, never stored. ``null`` when there is no suggestion.
        :type suggested_domains: [str], none_type, optional
        """
        if allowed_domains is not unset:
            kwargs["allowed_domains"] = allowed_domains
        if rules is not unset:
            kwargs["rules"] = rules
        if suggested_domains is not unset:
            kwargs["suggested_domains"] = suggested_domains
        super().__init__(kwargs)

        self_.mode = mode
