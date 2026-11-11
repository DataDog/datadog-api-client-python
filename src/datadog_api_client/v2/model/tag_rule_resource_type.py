# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagRuleResourceType(ModelSimple):
    """
    JSON:API resource type for a tag rule. Responses use the legacy `tag_policy` value.

    :param value: Must be one of ["tag_rule", "tag_policy"].
    :type value: str
    """

    allowed_values = {
        "tag_rule",
        "tag_policy",
    }
    TAG_RULE: ClassVar["TagRuleResourceType"]
    TAG_POLICY: ClassVar["TagRuleResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagRuleResourceType.TAG_RULE = TagRuleResourceType("tag_rule")
TagRuleResourceType.TAG_POLICY = TagRuleResourceType("tag_policy")
