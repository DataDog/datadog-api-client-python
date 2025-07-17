# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSocketDestinationEncoding(ModelSimple):
    """
    Encoding format for log events.

    :param value: Must be one of ["json", "raw_message"].
    :type value: str
    """

    allowed_values = {
        "json",
        "raw_message",
    }
    JSON: ClassVar["ObservabilityPipelineSocketDestinationEncoding"]
    RAW_MESSAGE: ClassVar["ObservabilityPipelineSocketDestinationEncoding"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSocketDestinationEncoding.JSON = ObservabilityPipelineSocketDestinationEncoding("json")
ObservabilityPipelineSocketDestinationEncoding.RAW_MESSAGE = ObservabilityPipelineSocketDestinationEncoding(
    "raw_message"
)
