# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DataObservabilityMonitorRunType(ModelSimple):
    """
    The JSON:API resource type for a data observability monitor run.

    :param value: If omitted defaults to "monitor_run". Must be one of ["monitor_run"].
    :type value: str
    """

    allowed_values = {
        "monitor_run",
    }
    MONITOR_RUN: ClassVar["DataObservabilityMonitorRunType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DataObservabilityMonitorRunType.MONITOR_RUN = DataObservabilityMonitorRunType("monitor_run")
