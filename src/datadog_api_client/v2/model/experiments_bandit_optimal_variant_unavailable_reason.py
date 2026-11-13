# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditOptimalVariantUnavailableReason(ModelSimple):
    """
    Why no optimal variant is reported. Absent when one is, or when the cause isn't known.

    :param value: Must be one of ["NO_RESULTS_YET", "WARMUP", "NOT_ENOUGH_DATA", "NO_DIFFERENCE", "STATS_UNAVAILABLE"].
    :type value: str
    """

    allowed_values = {
        "NO_RESULTS_YET",
        "WARMUP",
        "NOT_ENOUGH_DATA",
        "NO_DIFFERENCE",
        "STATS_UNAVAILABLE",
    }
    NO_RESULTS_YET: ClassVar["ExperimentsBanditOptimalVariantUnavailableReason"]
    WARMUP: ClassVar["ExperimentsBanditOptimalVariantUnavailableReason"]
    NOT_ENOUGH_DATA: ClassVar["ExperimentsBanditOptimalVariantUnavailableReason"]
    NO_DIFFERENCE: ClassVar["ExperimentsBanditOptimalVariantUnavailableReason"]
    STATS_UNAVAILABLE: ClassVar["ExperimentsBanditOptimalVariantUnavailableReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditOptimalVariantUnavailableReason.NO_RESULTS_YET = ExperimentsBanditOptimalVariantUnavailableReason(
    "NO_RESULTS_YET"
)
ExperimentsBanditOptimalVariantUnavailableReason.WARMUP = ExperimentsBanditOptimalVariantUnavailableReason("WARMUP")
ExperimentsBanditOptimalVariantUnavailableReason.NOT_ENOUGH_DATA = ExperimentsBanditOptimalVariantUnavailableReason(
    "NOT_ENOUGH_DATA"
)
ExperimentsBanditOptimalVariantUnavailableReason.NO_DIFFERENCE = ExperimentsBanditOptimalVariantUnavailableReason(
    "NO_DIFFERENCE"
)
ExperimentsBanditOptimalVariantUnavailableReason.STATS_UNAVAILABLE = ExperimentsBanditOptimalVariantUnavailableReason(
    "STATS_UNAVAILABLE"
)
