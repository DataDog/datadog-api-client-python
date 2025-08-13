# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding(ModelSimple):
    """
    Encoding format for log events.

    :param value: Must be one of ["json", "raw_message"].
    :type value: str
    """

    allowed_values = {
        "json",
        "raw_message",
    }
    JSON: ClassVar["ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding"]
    RAW_MESSAGE: ClassVar["ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding.JSON = (
    ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding("json")
)
ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding.RAW_MESSAGE = (
    ObservabilityPipelineCrowdStrikeNextGenSiemDestinationEncoding("raw_message")
)
