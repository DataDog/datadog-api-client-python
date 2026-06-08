# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagIndexingRuleExemptionType(ModelSimple):
    """
    The tag indexing rule exemption resource type.

    :param value: If omitted defaults to "tag_indexing_rule_exemptions". Must be one of ["tag_indexing_rule_exemptions"].
    :type value: str
    """

    allowed_values = {
        "tag_indexing_rule_exemptions",
    }
    TAG_INDEXING_RULE_EXEMPTIONS: ClassVar["TagIndexingRuleExemptionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagIndexingRuleExemptionType.TAG_INDEXING_RULE_EXEMPTIONS = TagIndexingRuleExemptionType("tag_indexing_rule_exemptions")
