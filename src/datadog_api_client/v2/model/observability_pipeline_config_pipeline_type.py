# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineConfigPipelineType(ModelSimple):
    """
    The type of data being ingested. Defaults to `logs` if not specified.

    :param value: If omitted defaults to "logs". Must be one of ["logs", "metrics"].
    :type value: str
    """

    allowed_values = {
        "logs",
        "metrics",
    }
    LOGS: ClassVar["ObservabilityPipelineConfigPipelineType"]
    METRICS: ClassVar["ObservabilityPipelineConfigPipelineType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineConfigPipelineType.LOGS = ObservabilityPipelineConfigPipelineType("logs")
ObservabilityPipelineConfigPipelineType.METRICS = ObservabilityPipelineConfigPipelineType("metrics")
