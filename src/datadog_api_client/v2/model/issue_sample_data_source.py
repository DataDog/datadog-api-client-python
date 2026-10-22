# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueSampleDataSource(ModelSimple):
    """
    Product that reported the error. `NONE` when the error has no known origin.

    :param value: Must be one of ["APM", "LOGS", "RUM", "LLMOBS", "SYNTHETICS", "NONE"].
    :type value: str
    """

    allowed_values = {
        "APM",
        "LOGS",
        "RUM",
        "LLMOBS",
        "SYNTHETICS",
        "NONE",
    }
    APM: ClassVar["IssueSampleDataSource"]
    LOGS: ClassVar["IssueSampleDataSource"]
    RUM: ClassVar["IssueSampleDataSource"]
    LLMOBS: ClassVar["IssueSampleDataSource"]
    SYNTHETICS: ClassVar["IssueSampleDataSource"]
    NONE: ClassVar["IssueSampleDataSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueSampleDataSource.APM = IssueSampleDataSource("APM")
IssueSampleDataSource.LOGS = IssueSampleDataSource("LOGS")
IssueSampleDataSource.RUM = IssueSampleDataSource("RUM")
IssueSampleDataSource.LLMOBS = IssueSampleDataSource("LLMOBS")
IssueSampleDataSource.SYNTHETICS = IssueSampleDataSource("SYNTHETICS")
IssueSampleDataSource.NONE = IssueSampleDataSource("NONE")
