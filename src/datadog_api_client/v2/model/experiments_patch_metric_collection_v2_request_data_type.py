# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsPatchMetricCollectionV2RequestDataType(ModelSimple):
    """
    Metric collections resource type.

    :param value: If omitted defaults to "metric-collections". Must be one of ["metric-collections"].
    :type value: str
    """

    allowed_values = {
        "metric-collections",
    }
    METRIC_COLLECTIONS: ClassVar["ExperimentsPatchMetricCollectionV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsPatchMetricCollectionV2RequestDataType.METRIC_COLLECTIONS = (
    ExperimentsPatchMetricCollectionV2RequestDataType("metric-collections")
)
