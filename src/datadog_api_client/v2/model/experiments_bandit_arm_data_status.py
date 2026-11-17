# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditArmDataStatus(ModelSimple):
    """
    Where the arm's reward variance came from, or why it's unavailable.

    :param value: Must be one of ["usable", "insufficient_data", "zero_variance", "pooled_within_variance", "pooled_total_variance"].
    :type value: str
    """

    allowed_values = {
        "usable",
        "insufficient_data",
        "zero_variance",
        "pooled_within_variance",
        "pooled_total_variance",
    }
    USABLE: ClassVar["ExperimentsBanditArmDataStatus"]
    INSUFFICIENT_DATA: ClassVar["ExperimentsBanditArmDataStatus"]
    ZERO_VARIANCE: ClassVar["ExperimentsBanditArmDataStatus"]
    POOLED_WITHIN_VARIANCE: ClassVar["ExperimentsBanditArmDataStatus"]
    POOLED_TOTAL_VARIANCE: ClassVar["ExperimentsBanditArmDataStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditArmDataStatus.USABLE = ExperimentsBanditArmDataStatus("usable")
ExperimentsBanditArmDataStatus.INSUFFICIENT_DATA = ExperimentsBanditArmDataStatus("insufficient_data")
ExperimentsBanditArmDataStatus.ZERO_VARIANCE = ExperimentsBanditArmDataStatus("zero_variance")
ExperimentsBanditArmDataStatus.POOLED_WITHIN_VARIANCE = ExperimentsBanditArmDataStatus("pooled_within_variance")
ExperimentsBanditArmDataStatus.POOLED_TOTAL_VARIANCE = ExperimentsBanditArmDataStatus("pooled_total_variance")
