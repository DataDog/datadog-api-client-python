# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicyType(ModelSimple):
    """
    Org group policies resource type.

    :param value: If omitted defaults to "org_group_policies". Must be one of ["org_group_policies"].
    :type value: str
    """

    allowed_values = {
        "org_group_policies",
    }
    ORG_GROUP_POLICIES: ClassVar["OrgGroupPolicyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicyType.ORG_GROUP_POLICIES = OrgGroupPolicyType("org_group_policies")
