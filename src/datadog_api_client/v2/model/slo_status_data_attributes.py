# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.raw_error_budget_remaining import RawErrorBudgetRemaining


class SloStatusDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.raw_error_budget_remaining import RawErrorBudgetRemaining

        return {
            "error_budget_remaining": (float,),
            "raw_error_budget_remaining": (RawErrorBudgetRemaining,),
            "sli": (float,),
            "span_precision": (int,),
            "state": (str,),
        }

    attribute_map = {
        "error_budget_remaining": "error_budget_remaining",
        "raw_error_budget_remaining": "raw_error_budget_remaining",
        "sli": "sli",
        "span_precision": "span_precision",
        "state": "state",
    }

    def __init__(
        self_,
        error_budget_remaining: float,
        raw_error_budget_remaining: RawErrorBudgetRemaining,
        sli: float,
        span_precision: int,
        state: str,
        **kwargs,
    ):
        """
        The attributes of the SLO status.

        :param error_budget_remaining: The percentage of error budget remaining.
        :type error_budget_remaining: float

        :param raw_error_budget_remaining: The raw error budget remaining for the SLO.
        :type raw_error_budget_remaining: RawErrorBudgetRemaining

        :param sli: The current Service Level Indicator (SLI) value as a percentage.
        :type sli: float

        :param span_precision: The precision of the time span in seconds.
        :type span_precision: int

        :param state: The current state of the SLO (for example, ``breached`` , ``warning`` , ``ok`` ).
        :type state: str
        """
        super().__init__(kwargs)

        self_.error_budget_remaining = error_budget_remaining
        self_.raw_error_budget_remaining = raw_error_budget_remaining
        self_.sli = sli
        self_.span_precision = span_precision
        self_.state = state
