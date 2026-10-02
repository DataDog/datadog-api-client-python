# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsCreateMetricV2RequestDataAttributesDesiredChange(ModelSimple):
    """
    Direction of change that represents an improvement for this metric.

    :param value: Must be one of ["METRIC_INCREASES", "METRIC_DECREASES"].
    :type value: str
    """

    allowed_values = {
        "METRIC_INCREASES",
        "METRIC_DECREASES",
    }
    METRIC_INCREASES: ClassVar["ExperimentsCreateMetricV2RequestDataAttributesDesiredChange"]
    METRIC_DECREASES: ClassVar["ExperimentsCreateMetricV2RequestDataAttributesDesiredChange"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsCreateMetricV2RequestDataAttributesDesiredChange.METRIC_INCREASES = (
    ExperimentsCreateMetricV2RequestDataAttributesDesiredChange("METRIC_INCREASES")
)
ExperimentsCreateMetricV2RequestDataAttributesDesiredChange.METRIC_DECREASES = (
    ExperimentsCreateMetricV2RequestDataAttributesDesiredChange("METRIC_DECREASES")
)
