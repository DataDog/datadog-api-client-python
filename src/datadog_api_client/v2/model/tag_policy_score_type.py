# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagPolicyScoreType(ModelSimple):
    """
    The type of the resource. The value should always be `tag_policy_score`.

    :param value: If omitted defaults to "tag_policy_score". Must be one of ["tag_policy_score"].
    :type value: str
    """

    allowed_values = {
        "tag_policy_score",
    }
    TAG_POLICY_SCORE: ClassVar["TagPolicyScoreType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagPolicyScoreType.TAG_POLICY_SCORE = TagPolicyScoreType("tag_policy_score")
