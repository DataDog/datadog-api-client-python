# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelinePrometheusRemoteWriteSourceType(ModelSimple):
    """
    The source type. The value should always be `prometheus_remote_write`.

    :param value: If omitted defaults to "prometheus_remote_write". Must be one of ["prometheus_remote_write"].
    :type value: str
    """

    allowed_values = {
        "prometheus_remote_write",
    }
    PROMETHEUS_REMOTE_WRITE: ClassVar["ObservabilityPipelinePrometheusRemoteWriteSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelinePrometheusRemoteWriteSourceType.PROMETHEUS_REMOTE_WRITE = (
    ObservabilityPipelinePrometheusRemoteWriteSourceType("prometheus_remote_write")
)
