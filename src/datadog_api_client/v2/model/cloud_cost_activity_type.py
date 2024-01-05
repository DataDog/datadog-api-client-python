# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudCostActivityType(ModelSimple):
    """
    Type of Cloud Cost Activity.

    :param value: If omitted defaults to "cloud_cost_activity". Must be one of ["cloud_cost_activity"].
    :type value: str
    """

    allowed_values = {
        "cloud_cost_activity",
    }
    CLOUD_COST_ACTIVITY: ClassVar["CloudCostActivityType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudCostActivityType.CLOUD_COST_ACTIVITY = CloudCostActivityType("cloud_cost_activity")
