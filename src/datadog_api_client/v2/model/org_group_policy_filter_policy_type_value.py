# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicyFilterPolicyTypeValue(ModelSimple):
    """
    The type of the policy to filter by. `org_config` indicates a policy backed by an organization configuration setting. `role` indicates a policy backed by a Datadog custom role.

    :param value: Must be one of ["org_config", "role"].
    :type value: str
    """

    allowed_values = {
        "org_config",
        "role",
    }
    ORG_CONFIG: ClassVar["OrgGroupPolicyFilterPolicyTypeValue"]
    ROLE: ClassVar["OrgGroupPolicyFilterPolicyTypeValue"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicyFilterPolicyTypeValue.ORG_CONFIG = OrgGroupPolicyFilterPolicyTypeValue("org_config")
OrgGroupPolicyFilterPolicyTypeValue.ROLE = OrgGroupPolicyFilterPolicyTypeValue("role")
