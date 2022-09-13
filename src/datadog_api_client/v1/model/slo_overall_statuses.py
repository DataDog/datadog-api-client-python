# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class SLOOverallStatuses(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_raw_error_budget_remaining import SLORawErrorBudgetRemaining
        from datadog_api_client.v1.model.slo_timeframe import SLOTimeframe

        return {
            "error": (str, none_type),
            "indexed_at": (int,),
            "raw_error_budget_remaining": (SLORawErrorBudgetRemaining,),
            "span_precision": (int,),
            "status": (float, none_type),
            "target": (float,),
            "timeframe": (SLOTimeframe,),
        }

    attribute_map = {
        "error": "error",
        "indexed_at": "indexed_at",
        "raw_error_budget_remaining": "raw_error_budget_remaining",
        "span_precision": "span_precision",
        "status": "status",
        "target": "target",
        "timeframe": "timeframe",
    }

    def __init__(self_, *args, **kwargs):
        """
        Overall status of the SLO by timeframes.

        :param error: Error message if SLO status or error budget could not be calculated.
        :type error: str, none_type, optional

        :param indexed_at: timestamp (UNIX time in seconds) of when the SLO status and error budget
            were calculated.
        :type indexed_at: int, optional

        :param raw_error_budget_remaining: Error budget remaining for an SLO.
        :type raw_error_budget_remaining: SLORawErrorBudgetRemaining, optional

        :param span_precision: The amount of decimal places the SLI value is accurate to.
        :type span_precision: int, optional

        :param status: The status of the SLO.
        :type status: float, none_type, optional

        :param target: The target of the SLO.
        :type target: float, optional

        :param timeframe: The SLO time window options.
        :type timeframe: SLOTimeframe, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
