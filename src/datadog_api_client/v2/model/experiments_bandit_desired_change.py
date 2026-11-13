# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditDesiredChange(ModelSimple):
    """
    The direction the bandit optimizes the metric in. It's fixed when the bandit starts. Null before the first saved refresh.

    :param value: Must be one of ["METRIC_INCREASES", "METRIC_DECREASES"].
    :type value: str
    """

    allowed_values = {
        "METRIC_INCREASES",
        "METRIC_DECREASES",
    }
    METRIC_INCREASES: ClassVar["ExperimentsBanditDesiredChange"]
    METRIC_DECREASES: ClassVar["ExperimentsBanditDesiredChange"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditDesiredChange.METRIC_INCREASES = ExperimentsBanditDesiredChange("METRIC_INCREASES")
ExperimentsBanditDesiredChange.METRIC_DECREASES = ExperimentsBanditDesiredChange("METRIC_DECREASES")
