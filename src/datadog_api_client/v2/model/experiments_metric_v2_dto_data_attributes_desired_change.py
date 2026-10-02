# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsMetricV2DTODataAttributesDesiredChange(ModelSimple):
    """
    Direction of metric change considered desirable.

    :param value: Must be one of ["METRIC_INCREASES", "METRIC_DECREASES", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "METRIC_INCREASES",
        "METRIC_DECREASES",
        "UNKNOWN",
    }
    METRIC_INCREASES: ClassVar["ExperimentsMetricV2DTODataAttributesDesiredChange"]
    METRIC_DECREASES: ClassVar["ExperimentsMetricV2DTODataAttributesDesiredChange"]
    UNKNOWN: ClassVar["ExperimentsMetricV2DTODataAttributesDesiredChange"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsMetricV2DTODataAttributesDesiredChange.METRIC_INCREASES = ExperimentsMetricV2DTODataAttributesDesiredChange(
    "METRIC_INCREASES"
)
ExperimentsMetricV2DTODataAttributesDesiredChange.METRIC_DECREASES = ExperimentsMetricV2DTODataAttributesDesiredChange(
    "METRIC_DECREASES"
)
ExperimentsMetricV2DTODataAttributesDesiredChange.UNKNOWN = ExperimentsMetricV2DTODataAttributesDesiredChange("UNKNOWN")
