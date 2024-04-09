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

    :param value: Must be one of ["in_progress", "completed", "completed_with_errors", "failed"].
    :type value: str
    """

    allowed_values = {
        "in_progress",
        "completed",
        "completed_with_errors",
        "failed",
    }
    IN_PROGRESS: ClassVar["SLOReportStatus"]
    COMPLETED: ClassVar["SLOReportStatus"]
    COMPLETED_WITH_ERRORS: ClassVar["SLOReportStatus"]
    FAILED: ClassVar["SLOReportStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SLOReportStatus.IN_PROGRESS = SLOReportStatus("in_progress")
SLOReportStatus.COMPLETED = SLOReportStatus("completed")
SLOReportStatus.COMPLETED_WITH_ERRORS = SLOReportStatus("completed_with_errors")
SLOReportStatus.FAILED = SLOReportStatus("failed")
