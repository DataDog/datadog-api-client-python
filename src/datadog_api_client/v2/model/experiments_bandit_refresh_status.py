# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditRefreshStatus(ModelSimple):
    """
    The status of the refresh.

    :param value: Must be one of ["PENDING", "RUNNING", "SUCCEEDED", "FAILED", "CANCELLED"].
    :type value: str
    """

    allowed_values = {
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
    }
    PENDING: ClassVar["ExperimentsBanditRefreshStatus"]
    RUNNING: ClassVar["ExperimentsBanditRefreshStatus"]
    SUCCEEDED: ClassVar["ExperimentsBanditRefreshStatus"]
    FAILED: ClassVar["ExperimentsBanditRefreshStatus"]
    CANCELLED: ClassVar["ExperimentsBanditRefreshStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditRefreshStatus.PENDING = ExperimentsBanditRefreshStatus("PENDING")
ExperimentsBanditRefreshStatus.RUNNING = ExperimentsBanditRefreshStatus("RUNNING")
ExperimentsBanditRefreshStatus.SUCCEEDED = ExperimentsBanditRefreshStatus("SUCCEEDED")
ExperimentsBanditRefreshStatus.FAILED = ExperimentsBanditRefreshStatus("FAILED")
ExperimentsBanditRefreshStatus.CANCELLED = ExperimentsBanditRefreshStatus("CANCELLED")
