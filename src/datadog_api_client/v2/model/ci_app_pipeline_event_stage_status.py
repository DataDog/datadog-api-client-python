# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CIAppPipelineEventStageStatus(ModelSimple):
    """
    The final status of the stage.

    :param value: Must be one of ["success", "error", "canceled", "skipped"].
    :type value: str
    """

    allowed_values = {
        "success",
        "error",
        "canceled",
        "skipped",
    }
    SUCCESS: ClassVar["CIAppPipelineEventStageStatus"]
    ERROR: ClassVar["CIAppPipelineEventStageStatus"]
    CANCELED: ClassVar["CIAppPipelineEventStageStatus"]
    SKIPPED: ClassVar["CIAppPipelineEventStageStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CIAppPipelineEventStageStatus.SUCCESS = CIAppPipelineEventStageStatus("success")
CIAppPipelineEventStageStatus.ERROR = CIAppPipelineEventStageStatus("error")
CIAppPipelineEventStageStatus.CANCELED = CIAppPipelineEventStageStatus("canceled")
CIAppPipelineEventStageStatus.SKIPPED = CIAppPipelineEventStageStatus("skipped")
