# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SLOReportStatus(ModelSimple):
    """
    The status of the SLO report job.

    :param value: Must be one of ["IN_PROGRESS", "COMPLETED", "COMPLETED_WITH_ERRORS", "FAILED", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "IN_PROGRESS",
        "COMPLETED",
        "COMPLETED_WITH_ERRORS",
        "FAILED",
        "UNKNOWN",
    }
    IN_PROGRESS: ClassVar["SLOReportStatus"]
    COMPLETED: ClassVar["SLOReportStatus"]
    COMPLETED_WITH_ERRORS: ClassVar["SLOReportStatus"]
    FAILED: ClassVar["SLOReportStatus"]
    UNKNOWN: ClassVar["SLOReportStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SLOReportStatus.IN_PROGRESS = SLOReportStatus("IN_PROGRESS")
SLOReportStatus.COMPLETED = SLOReportStatus("COMPLETED")
SLOReportStatus.COMPLETED_WITH_ERRORS = SLOReportStatus("COMPLETED_WITH_ERRORS")
SLOReportStatus.FAILED = SLOReportStatus("FAILED")
SLOReportStatus.UNKNOWN = SLOReportStatus("UNKNOWN")
