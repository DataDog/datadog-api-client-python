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


class OrgGroupPolicyAttributes(ModelNormal):
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
            "modified_at": (datetime,),
            "policy_name": (str,),
            "policy_type": (OrgGroupPolicyPolicyType,),
        }

    attribute_map = {
        "content": "content",
        "enforcement_tier": "enforcement_tier",
        "modified_at": "modified_at",
        "policy_name": "policy_name",
        "policy_type": "policy_type",
    }

    def __init__(
        self_,
        enforcement_tier: OrgGroupPolicyEnforcementTier,
        modified_at: datetime,
        policy_name: str,
        policy_type: OrgGroupPolicyPolicyType,
        content: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an org group policy.

        :param content: The policy content as key-value pairs.
        :type content: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param enforcement_tier: The enforcement tier of the policy. ``DEFAULT`` means the policy is set but member orgs may mutate it. ``ENFORCE`` means the policy is strictly controlled and mutations are blocked for affected orgs. ``DELEGATE`` means each member org controls its own value.
        :type enforcement_tier: OrgGroupPolicyEnforcementTier

        :param modified_at: Timestamp when the policy was last modified.
        :type modified_at: datetime

        :param policy_name: The name of the policy.
        :type policy_name: str

        :param policy_type: The type of the policy. Only ``org_config`` is supported, indicating a policy backed by an organization configuration setting.
        :type policy_type: OrgGroupPolicyPolicyType
        """
        if content is not unset:
            kwargs["content"] = content
        super().__init__(kwargs)

        self_.enforcement_tier = enforcement_tier
        self_.modified_at = modified_at
        self_.policy_name = policy_name
        self_.policy_type = policy_type
