# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UnitCostType(ModelSimple):
    """
    The JSON:API resource type for a unit cost.

    :param value: If omitted defaults to "unit_cost". Must be one of ["unit_cost"].
    :type value: str
    """

    allowed_values = {
        "unit_cost",
    }
    UNIT_COST: ClassVar["UnitCostType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UnitCostType.UNIT_COST = UnitCostType("unit_cost")
