# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RawErrorBudgetRemaining(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "unit": (str,),
            "value": (float,),
        }

    attribute_map = {
        "unit": "unit",
        "value": "value",
    }

    def __init__(self_, unit: str, value: float, **kwargs):
        """
        The raw error budget remaining for the SLO.

        :param unit: The unit of the error budget (for example, ``seconds`` , ``requests`` ).
        :type unit: str

        :param value: The numeric value of the remaining error budget.
        :type value: float
        """
        super().__init__(kwargs)

        self_.unit = unit
        self_.value = value
