# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostTagPipelineActiveKeyType(ModelSimple):
    """
    Active tag key resource type.

    :param value: If omitted defaults to "active_tag_key". Must be one of ["active_tag_key"].
    :type value: str
    """

    allowed_values = {
        "active_tag_key",
    }
    ACTIVE_TAG_KEY: ClassVar["CostTagPipelineActiveKeyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostTagPipelineActiveKeyType.ACTIVE_TAG_KEY = CostTagPipelineActiveKeyType("active_tag_key")
