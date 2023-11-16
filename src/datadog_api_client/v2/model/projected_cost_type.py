# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProjectedCostType(ModelSimple):
    """
    Type of cost data.

    :param value: If omitted defaults to "projected_cost". Must be one of ["projected_cost"].
    :type value: str
    """

    allowed_values = {
        "projected_cost",
    }
    PROJECt_COST: ClassVar["ProjectedCostType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProjectedCostType.PROJECt_COST = ProjectedCostType("projected_cost")
