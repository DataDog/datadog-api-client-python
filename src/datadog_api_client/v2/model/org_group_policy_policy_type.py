# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicyPolicyType(ModelSimple):
    """
    The type of the policy. `org_config` indicates a policy backed by an organization configuration setting. `role` indicates a policy backed by a Datadog custom role.

    :param value: If omitted defaults to "org_config". Must be one of ["org_config", "role"].
    :type value: str
    """

    allowed_values = {
        "org_config",
        "role",
    }
    ORG_CONFIG: ClassVar["OrgGroupPolicyPolicyType"]
    ROLE: ClassVar["OrgGroupPolicyPolicyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicyPolicyType.ORG_CONFIG = OrgGroupPolicyPolicyType("org_config")
OrgGroupPolicyPolicyType.ROLE = OrgGroupPolicyPolicyType("role")
