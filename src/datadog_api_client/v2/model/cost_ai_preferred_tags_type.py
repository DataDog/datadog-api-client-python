# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostAIPreferredTagsType(ModelSimple):
    """
    Preferred tags resource type.

    :param value: If omitted defaults to "preferred_tags". Must be one of ["preferred_tags"].
    :type value: str
    """

    allowed_values = {
        "preferred_tags",
    }
    PREFERRED_TAGS: ClassVar["CostAIPreferredTagsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostAIPreferredTagsType.PREFERRED_TAGS = CostAIPreferredTagsType("preferred_tags")
