# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineSumoLogicDestinationEncoding(ModelSimple):
    """
    The output encoding format.

    :param value: Must be one of ["json", "raw_message", "logfmt"].
    :type value: str
    """

    allowed_values = {
        "json",
        "raw_message",
        "logfmt",
    }
    JSON: ClassVar["ObservabilityPipelineSumoLogicDestinationEncoding"]
    RAW_MESSAGE: ClassVar["ObservabilityPipelineSumoLogicDestinationEncoding"]
    LOGFMT: ClassVar["ObservabilityPipelineSumoLogicDestinationEncoding"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineSumoLogicDestinationEncoding.JSON = ObservabilityPipelineSumoLogicDestinationEncoding("json")
ObservabilityPipelineSumoLogicDestinationEncoding.RAW_MESSAGE = ObservabilityPipelineSumoLogicDestinationEncoding(
    "raw_message"
)
ObservabilityPipelineSumoLogicDestinationEncoding.LOGFMT = ObservabilityPipelineSumoLogicDestinationEncoding("logfmt")
