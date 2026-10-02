# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsPatchExperimentMetricGroupV2RequestDataType(ModelSimple):
    """
    Experiment metric groups resource type.

    :param value: If omitted defaults to "experiment-metric-groups". Must be one of ["experiment-metric-groups"].
    :type value: str
    """

    allowed_values = {
        "experiment-metric-groups",
    }
    EXPERIMENT_METRIC_GROUPS: ClassVar["ExperimentsPatchExperimentMetricGroupV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsPatchExperimentMetricGroupV2RequestDataType.EXPERIMENT_METRIC_GROUPS = (
    ExperimentsPatchExperimentMetricGroupV2RequestDataType("experiment-metric-groups")
)
