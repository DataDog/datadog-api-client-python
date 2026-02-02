# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagPolicyType(ModelSimple):
    """
    The type of the resource. The value should always be `tag_policy`.

    :param value: If omitted defaults to "tag_policy". Must be one of ["tag_policy"].
    :type value: str
    """

    allowed_values = {
        "tag_policy",
    }
    TAG_POLICY: ClassVar["TagPolicyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagPolicyType.TAG_POLICY = TagPolicyType("tag_policy")
