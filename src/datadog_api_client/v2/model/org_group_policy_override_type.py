# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicyOverrideType(ModelSimple):
    """
    Org group policy overrides resource type.

    :param value: If omitted defaults to "org_group_policy_overrides". Must be one of ["org_group_policy_overrides"].
    :type value: str
    """

    allowed_values = {
        "org_group_policy_overrides",
    }
    ORG_GROUP_POLICY_OVERRIDES: ClassVar["OrgGroupPolicyOverrideType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicyOverrideType.ORG_GROUP_POLICY_OVERRIDES = OrgGroupPolicyOverrideType("org_group_policy_overrides")
