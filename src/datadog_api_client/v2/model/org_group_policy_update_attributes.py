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


class OrgGroupPolicyUpdateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_group_policy_enforcement_tier import OrgGroupPolicyEnforcementTier

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
        }

    attribute_map = {
        "content": "content",
        "enforcement_tier": "enforcement_tier",
    }

    def __init__(
        self_,
        content: Union[Dict[str, Any], UnsetType] = unset,
        enforcement_tier: Union[OrgGroupPolicyEnforcementTier, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating an org group policy.

        :param content: The policy content as key-value pairs.
        :type content: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param enforcement_tier: The enforcement tier of the policy. ``DEFAULT`` means the policy is set but member orgs may mutate it. ``ENFORCE`` means the policy is strictly controlled and mutations are blocked for affected orgs. ``DELEGATE`` means each member org controls its own value.
        :type enforcement_tier: OrgGroupPolicyEnforcementTier, optional
        """
        if content is not unset:
            kwargs["content"] = content
        if enforcement_tier is not unset:
            kwargs["enforcement_tier"] = enforcement_tier
        super().__init__(kwargs)
