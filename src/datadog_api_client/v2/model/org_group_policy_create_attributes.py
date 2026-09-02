# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_group_policy_enforcement_tier import OrgGroupPolicyEnforcementTier
    from datadog_api_client.v2.model.org_group_policy_policy_type import OrgGroupPolicyPolicyType


class OrgGroupPolicyCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_enforcement_tier import OrgGroupPolicyEnforcementTier
        from datadog_api_client.v2.model.org_group_policy_policy_type import OrgGroupPolicyPolicyType

        return {
            "content": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "enforcement_tier": (OrgGroupPolicyEnforcementTier,),
            "policy_name": (str,),
            "policy_type": (OrgGroupPolicyPolicyType,),
        }

    attribute_map = {
        "content": "content",
        "enforcement_tier": "enforcement_tier",
        "policy_name": "policy_name",
        "policy_type": "policy_type",
    }

    def __init__(
        self_,
        content: Dict[str, Any],
        policy_name: str,
        enforcement_tier: Union[OrgGroupPolicyEnforcementTier, UnsetType] = unset,
        policy_type: Union[OrgGroupPolicyPolicyType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an org group policy. If ``policy_type`` is not provided, it defaults to ``org_config``. ``enforcement_tier`` is optional; if not provided, the resulting value depends on ``policy_type`` and is otherwise unspecified.

        :param content: The policy content as key-value pairs. For ``org_config`` policies, an arbitrary key-value map (for example, ``{"value": "UTC"}`` ). For ``role`` policies, a ``permissions`` key containing an array of permission UUIDs (for example, ``{"permissions": ["<uuid>", ...]}`` ).
        :type content: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}

        :param enforcement_tier: The enforcement tier of the policy. ``OVERRIDE_ALLOWED`` means the policy is set but member orgs may mutate it. ``GROUP_MANAGED`` means the policy is strictly controlled and mutations are blocked for affected orgs. ``DELEGATE`` means each member org controls its own value. ``role`` policies only support ``GROUP_MANAGED`` and ``DELEGATE`` — ``OVERRIDE_ALLOWED`` is rejected for this policy type. Transitioning a ``role`` policy to ``DELEGATE`` (disabling it) is one-way — the policy cannot be transitioned back to ``GROUP_MANAGED`` afterward.
        :type enforcement_tier: OrgGroupPolicyEnforcementTier, optional

        :param policy_name: The name of the policy. This becomes the name of the resource created across orgs in the group (for example, for ``role`` policies, the name of the created role).
        :type policy_name: str

        :param policy_type: The type of the policy. ``org_config`` indicates a policy backed by an organization configuration setting. ``role`` indicates a policy backed by a Datadog custom role.
        :type policy_type: OrgGroupPolicyPolicyType, optional
        """
        if enforcement_tier is not unset:
            kwargs["enforcement_tier"] = enforcement_tier
        if policy_type is not unset:
            kwargs["policy_type"] = policy_type
        super().__init__(kwargs)

        self_.content = content
        self_.policy_name = policy_name
