# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicyEnforcementTier(ModelSimple):
    """
    The enforcement tier of the policy. `OVERRIDE_ALLOWED` means the policy is set but member orgs may mutate it. `GROUP_MANAGED` means the policy is strictly controlled and mutations are blocked for affected orgs. `DELEGATE` means each member org controls its own value.

    :param value: If omitted defaults to "OVERRIDE_ALLOWED". Must be one of ["OVERRIDE_ALLOWED", "GROUP_MANAGED", "DELEGATE"].
    :type value: str
    """

    allowed_values = {
        "OVERRIDE_ALLOWED",
        "GROUP_MANAGED",
        "DELEGATE",
    }
    OVERRIDE_ALLOWED: ClassVar["OrgGroupPolicyEnforcementTier"]
    GROUP_MANAGED: ClassVar["OrgGroupPolicyEnforcementTier"]
    DELEGATE: ClassVar["OrgGroupPolicyEnforcementTier"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicyEnforcementTier.OVERRIDE_ALLOWED = OrgGroupPolicyEnforcementTier("OVERRIDE_ALLOWED")
OrgGroupPolicyEnforcementTier.GROUP_MANAGED = OrgGroupPolicyEnforcementTier("GROUP_MANAGED")
OrgGroupPolicyEnforcementTier.DELEGATE = OrgGroupPolicyEnforcementTier("DELEGATE")
