# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormulaAndFunctionSLOMeasure(ModelSimple):
    """
    SLO measures queries.

    :param value: Must be one of ["good_events", "bad_events", "slo_status", "error_budget_remaining", "burn_rate", "error_budget_burndown"].
    :type value: str
    """

    allowed_values = {
        "good_events",
        "bad_events",
        "slo_status",
        "error_budget_remaining",
        "burn_rate",
        "error_budget_burndown",
    }
    GOOD_EVENTS: ClassVar["FormulaAndFunctionSLOMeasure"]
    BAD_EVENTS: ClassVar["FormulaAndFunctionSLOMeasure"]
    SLO_STATUS: ClassVar["FormulaAndFunctionSLOMeasure"]
    ERROR_BUDGET_REMAINING: ClassVar["FormulaAndFunctionSLOMeasure"]
    BURN_RATE: ClassVar["FormulaAndFunctionSLOMeasure"]
    ERROR_BUDGET_BURNDOWN: ClassVar["FormulaAndFunctionSLOMeasure"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormulaAndFunctionSLOMeasure.GOOD_EVENTS = FormulaAndFunctionSLOMeasure("good_events")
FormulaAndFunctionSLOMeasure.BAD_EVENTS = FormulaAndFunctionSLOMeasure("bad_events")
FormulaAndFunctionSLOMeasure.SLO_STATUS = FormulaAndFunctionSLOMeasure("slo_status")
FormulaAndFunctionSLOMeasure.ERROR_BUDGET_REMAINING = FormulaAndFunctionSLOMeasure("error_budget_remaining")
FormulaAndFunctionSLOMeasure.BURN_RATE = FormulaAndFunctionSLOMeasure("burn_rate")
FormulaAndFunctionSLOMeasure.ERROR_BUDGET_BURNDOWN = FormulaAndFunctionSLOMeasure("error_budget_burndown")
