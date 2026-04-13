# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicyOverrideSortOption(ModelSimple):
    """
    Field to sort overrides by.

    :param value: If omitted defaults to "id". Must be one of ["id", "-id", "org_uuid", "-org_uuid"].
    :type value: str
    """

    allowed_values = {
        "id",
        "-id",
        "org_uuid",
        "-org_uuid",
    }
    ID: ClassVar["OrgGroupPolicyOverrideSortOption"]
    MINUS_ID: ClassVar["OrgGroupPolicyOverrideSortOption"]
    ORG_UUID: ClassVar["OrgGroupPolicyOverrideSortOption"]
    MINUS_ORG_UUID: ClassVar["OrgGroupPolicyOverrideSortOption"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicyOverrideSortOption.ID = OrgGroupPolicyOverrideSortOption("id")
OrgGroupPolicyOverrideSortOption.MINUS_ID = OrgGroupPolicyOverrideSortOption("-id")
OrgGroupPolicyOverrideSortOption.ORG_UUID = OrgGroupPolicyOverrideSortOption("org_uuid")
OrgGroupPolicyOverrideSortOption.MINUS_ORG_UUID = OrgGroupPolicyOverrideSortOption("-org_uuid")
