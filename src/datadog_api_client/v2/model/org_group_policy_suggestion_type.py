# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OrgGroupPolicySuggestionType(ModelSimple):
    """
    Org group policy suggestions resource type.

    :param value: If omitted defaults to "org_group_policy_suggestions". Must be one of ["org_group_policy_suggestions"].
    :type value: str
    """

    allowed_values = {
        "org_group_policy_suggestions",
    }
    ORG_GROUP_POLICY_SUGGESTIONS: ClassVar["OrgGroupPolicySuggestionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OrgGroupPolicySuggestionType.ORG_GROUP_POLICY_SUGGESTIONS = OrgGroupPolicySuggestionType("org_group_policy_suggestions")
