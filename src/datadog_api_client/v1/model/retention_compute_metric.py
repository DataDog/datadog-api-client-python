# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RetentionComputeMetric(ModelSimple):
    """
    Metric for retention compute.

    :param value: Must be one of ["__dd.retention", "__dd.retention_rate"].
    :type value: str
    """

    allowed_values = {
        "__dd.retention",
        "__dd.retention_rate",
    }
    RETENTION: ClassVar["RetentionComputeMetric"]
    RETENTION_RATE: ClassVar["RetentionComputeMetric"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RetentionComputeMetric.RETENTION = RetentionComputeMetric("__dd.retention")
RetentionComputeMetric.RETENTION_RATE = RetentionComputeMetric("__dd.retention_rate")
