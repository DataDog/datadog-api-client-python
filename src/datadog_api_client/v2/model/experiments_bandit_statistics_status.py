# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditStatisticsStatus(ModelSimple):
    """
    Whether the latest saved refresh calculated its statistics. Absent for older refreshes.

    :param value: Must be one of ["calculated", "failed"].
    :type value: str
    """

    allowed_values = {
        "calculated",
        "failed",
    }
    CALCULATED: ClassVar["ExperimentsBanditStatisticsStatus"]
    FAILED: ClassVar["ExperimentsBanditStatisticsStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditStatisticsStatus.CALCULATED = ExperimentsBanditStatisticsStatus("calculated")
ExperimentsBanditStatisticsStatus.FAILED = ExperimentsBanditStatisticsStatus("failed")
