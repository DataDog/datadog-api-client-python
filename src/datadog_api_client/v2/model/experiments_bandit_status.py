# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsBanditStatus(ModelSimple):
    """
    The bandit's status. STOPPED means the bandit was stopped and serves the variant chosen then. COMPLETED means it reached its scheduled end and serves its fallback.

    :param value: Must be one of ["DRAFT", "SCHEDULED", "RUNNING", "PAUSED", "STOPPED", "COMPLETED"].
    :type value: str
    """

    allowed_values = {
        "DRAFT",
        "SCHEDULED",
        "RUNNING",
        "PAUSED",
        "STOPPED",
        "COMPLETED",
    }
    DRAFT: ClassVar["ExperimentsBanditStatus"]
    SCHEDULED: ClassVar["ExperimentsBanditStatus"]
    RUNNING: ClassVar["ExperimentsBanditStatus"]
    PAUSED: ClassVar["ExperimentsBanditStatus"]
    STOPPED: ClassVar["ExperimentsBanditStatus"]
    COMPLETED: ClassVar["ExperimentsBanditStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsBanditStatus.DRAFT = ExperimentsBanditStatus("DRAFT")
ExperimentsBanditStatus.SCHEDULED = ExperimentsBanditStatus("SCHEDULED")
ExperimentsBanditStatus.RUNNING = ExperimentsBanditStatus("RUNNING")
ExperimentsBanditStatus.PAUSED = ExperimentsBanditStatus("PAUSED")
ExperimentsBanditStatus.STOPPED = ExperimentsBanditStatus("STOPPED")
ExperimentsBanditStatus.COMPLETED = ExperimentsBanditStatus("COMPLETED")
