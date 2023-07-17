# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FindingStatus(ModelSimple):
    """
    The status of the finding.

    :param value: Must be one of ["critical", "high", "medium", "low", "info"].
    :type value: str
    """

    allowed_values = {
        "critical",
        "high",
        "medium",
        "low",
        "info",
    }
    CRITICAL: ClassVar["FindingStatus"]
    HIGH: ClassVar["FindingStatus"]
    MEDIUM: ClassVar["FindingStatus"]
    LOW: ClassVar["FindingStatus"]
    INFO: ClassVar["FindingStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FindingStatus.CRITICAL = FindingStatus("critical")
FindingStatus.HIGH = FindingStatus("high")
FindingStatus.MEDIUM = FindingStatus("medium")
FindingStatus.LOW = FindingStatus("low")
FindingStatus.INFO = FindingStatus("info")
