# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AggregatedSignalsProblemsRequestType(ModelSimple):
    """
    The JSON:API type for aggregated signals and problems requests.

    :param value: If omitted defaults to "aggregated_signals_problems". Must be one of ["aggregated_signals_problems"].
    :type value: str
    """

    allowed_values = {
        "aggregated_signals_problems",
    }
    AGGREGATED_SIGNALS_PROBLEMS: ClassVar["AggregatedSignalsProblemsRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AggregatedSignalsProblemsRequestType.AGGREGATED_SIGNALS_PROBLEMS = AggregatedSignalsProblemsRequestType(
    "aggregated_signals_problems"
)
