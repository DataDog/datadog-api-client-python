# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineDatadogLogsDestinationType(ModelSimple):
    """
    The destination type. The value should always be `datadog_logs`.

    :param value: If omitted defaults to "datadog_logs". Must be one of ["datadog_logs"].
    :type value: str
    """

    allowed_values = {
        "datadog_logs",
    }
    DATADOG_LOGS: ClassVar["ObservabilityPipelineDatadogLogsDestinationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineDatadogLogsDestinationType.DATADOG_LOGS = ObservabilityPipelineDatadogLogsDestinationType(
    "datadog_logs"
)
