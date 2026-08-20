# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsFormulaJourneyRequestType(ModelSimple):
    """
    The resource type identifier for a journey timeseries or scalar request.

    :param value: If omitted defaults to "formula_journey_request". Must be one of ["formula_journey_request"].
    :type value: str
    """

    allowed_values = {
        "formula_journey_request",
    }
    FORMULA_JOURNEY_REQUEST: ClassVar["ProductAnalyticsFormulaJourneyRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsFormulaJourneyRequestType.FORMULA_JOURNEY_REQUEST = ProductAnalyticsFormulaJourneyRequestType(
    "formula_journey_request"
)
