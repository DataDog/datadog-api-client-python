# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostAttributionType(ModelSimple):
    """
    Type of cost attribution data.

    :param value: If omitted defaults to "cost_by_tag". Must be one of ["cost_by_tag"].
    :type value: str
    """

    allowed_values = {
        "cost_by_tag",
    }
    COST_BY_TAG: ClassVar["CostAttributionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostAttributionType.COST_BY_TAG = CostAttributionType("cost_by_tag")
