# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostTagKeySourceType(ModelSimple):
    """
    Type of the Cloud Cost Management tag source resource.

    :param value: If omitted defaults to "cost_tag_key_source". Must be one of ["cost_tag_key_source"].
    :type value: str
    """

    allowed_values = {
        "cost_tag_key_source",
    }
    COST_TAG_KEY_SOURCE: ClassVar["CostTagKeySourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostTagKeySourceType.COST_TAG_KEY_SOURCE = CostTagKeySourceType("cost_tag_key_source")
