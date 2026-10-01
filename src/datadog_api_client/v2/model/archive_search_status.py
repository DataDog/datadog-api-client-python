# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ArchiveSearchStatus(ModelSimple):
    """
    Current state of an Archive Search.

    :param value: Must be one of ["RUNNING", "COMPLETED", "FAILED", "CANCELLED", "QUOTA_REACHED", "EXPIRED"].
    :type value: str
    """

    allowed_values = {
        "RUNNING",
        "COMPLETED",
        "FAILED",
        "CANCELLED",
        "QUOTA_REACHED",
        "EXPIRED",
    }
    RUNNING: ClassVar["ArchiveSearchStatus"]
    COMPLETED: ClassVar["ArchiveSearchStatus"]
    FAILED: ClassVar["ArchiveSearchStatus"]
    CANCELLED: ClassVar["ArchiveSearchStatus"]
    QUOTA_REACHED: ClassVar["ArchiveSearchStatus"]
    EXPIRED: ClassVar["ArchiveSearchStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ArchiveSearchStatus.RUNNING = ArchiveSearchStatus("RUNNING")
ArchiveSearchStatus.COMPLETED = ArchiveSearchStatus("COMPLETED")
ArchiveSearchStatus.FAILED = ArchiveSearchStatus("FAILED")
ArchiveSearchStatus.CANCELLED = ArchiveSearchStatus("CANCELLED")
ArchiveSearchStatus.QUOTA_REACHED = ArchiveSearchStatus("QUOTA_REACHED")
ArchiveSearchStatus.EXPIRED = ArchiveSearchStatus("EXPIRED")
