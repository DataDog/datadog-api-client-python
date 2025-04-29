# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineGoogleChronicleDestinationEncoding(ModelSimple):
    """
    The encoding format for the logs sent to Chronicle.

    :param value: Must be one of ["json", "raw_message"].
    :type value: str
    """

    allowed_values = {
        "json",
        "raw_message",
    }
    JSON: ClassVar["ObservabilityPipelineGoogleChronicleDestinationEncoding"]
    RAW_MESSAGE: ClassVar["ObservabilityPipelineGoogleChronicleDestinationEncoding"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineGoogleChronicleDestinationEncoding.JSON = ObservabilityPipelineGoogleChronicleDestinationEncoding(
    "json"
)
ObservabilityPipelineGoogleChronicleDestinationEncoding.RAW_MESSAGE = (
    ObservabilityPipelineGoogleChronicleDestinationEncoding("raw_message")
)
