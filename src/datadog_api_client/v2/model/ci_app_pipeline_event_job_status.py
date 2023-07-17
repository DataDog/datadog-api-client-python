# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CIAppPipelineEventJobStatus(ModelSimple):
    """
    The final status of the job.

    :param value: Must be one of ["success", "error", "canceled", "skipped"].
    :type value: str
    """

    allowed_values = {
        "success",
        "error",
        "canceled",
        "skipped",
    }
    SUCCESS: ClassVar["CIAppPipelineEventJobStatus"]
    ERROR: ClassVar["CIAppPipelineEventJobStatus"]
    CANCELED: ClassVar["CIAppPipelineEventJobStatus"]
    SKIPPED: ClassVar["CIAppPipelineEventJobStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CIAppPipelineEventJobStatus.SUCCESS = CIAppPipelineEventJobStatus("success")
CIAppPipelineEventJobStatus.ERROR = CIAppPipelineEventJobStatus("error")
CIAppPipelineEventJobStatus.CANCELED = CIAppPipelineEventJobStatus("canceled")
CIAppPipelineEventJobStatus.SKIPPED = CIAppPipelineEventJobStatus("skipped")
