# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostCurrencyType(ModelSimple):
    """
    Type of the Cloud Cost Management billing currency resource.

    :param value: If omitted defaults to "cost_currency". Must be one of ["cost_currency"].
    :type value: str
    """

    allowed_values = {
        "cost_currency",
    }
    COST_CURRENCY: ClassVar["CostCurrencyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostCurrencyType.COST_CURRENCY = CostCurrencyType("cost_currency")
