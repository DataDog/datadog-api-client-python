# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CIAppPipelineEventPipelineStatus(ModelSimple):
    """
    The final status of the pipeline.

    :param value: Must be one of ["success", "error", "canceled", "skipped", "blocked"].
    :type value: str
    """

    allowed_values = {
        "success",
        "error",
        "canceled",
        "skipped",
        "blocked",
    }
    SUCCESS: ClassVar["CIAppPipelineEventPipelineStatus"]
    ERROR: ClassVar["CIAppPipelineEventPipelineStatus"]
    CANCELED: ClassVar["CIAppPipelineEventPipelineStatus"]
    SKIPPED: ClassVar["CIAppPipelineEventPipelineStatus"]
    BLOCKED: ClassVar["CIAppPipelineEventPipelineStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CIAppPipelineEventPipelineStatus.SUCCESS = CIAppPipelineEventPipelineStatus("success")
CIAppPipelineEventPipelineStatus.ERROR = CIAppPipelineEventPipelineStatus("error")
CIAppPipelineEventPipelineStatus.CANCELED = CIAppPipelineEventPipelineStatus("canceled")
CIAppPipelineEventPipelineStatus.SKIPPED = CIAppPipelineEventPipelineStatus("skipped")
CIAppPipelineEventPipelineStatus.BLOCKED = CIAppPipelineEventPipelineStatus("blocked")
