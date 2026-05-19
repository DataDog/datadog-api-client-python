# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ModelLabRunStatus(ModelSimple):
    """
    The status of a Model Lab run.

    :param value: Must be one of ["pending", "running", "completed", "failed", "killed", "unresponsive", "paused"].
    :type value: str
    """

    allowed_values = {
        "pending",
        "running",
        "completed",
        "failed",
        "killed",
        "unresponsive",
        "paused",
    }
    PENDING: ClassVar["ModelLabRunStatus"]
    RUNNING: ClassVar["ModelLabRunStatus"]
    COMPLETED: ClassVar["ModelLabRunStatus"]
    FAILED: ClassVar["ModelLabRunStatus"]
    KILLED: ClassVar["ModelLabRunStatus"]
    UNRESPONSIVE: ClassVar["ModelLabRunStatus"]
    PAUSED: ClassVar["ModelLabRunStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ModelLabRunStatus.PENDING = ModelLabRunStatus("pending")
ModelLabRunStatus.RUNNING = ModelLabRunStatus("running")
ModelLabRunStatus.COMPLETED = ModelLabRunStatus("completed")
ModelLabRunStatus.FAILED = ModelLabRunStatus("failed")
ModelLabRunStatus.KILLED = ModelLabRunStatus("killed")
ModelLabRunStatus.UNRESPONSIVE = ModelLabRunStatus("unresponsive")
ModelLabRunStatus.PAUSED = ModelLabRunStatus("paused")
