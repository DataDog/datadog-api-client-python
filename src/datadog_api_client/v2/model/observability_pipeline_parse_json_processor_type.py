# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineParseJSONProcessorType(ModelSimple):
    """
    The processor type. The value should always be `parse_json`.

    :param value: If omitted defaults to "parse_json". Must be one of ["parse_json"].
    :type value: str
    """

    allowed_values = {
        "parse_json",
    }
    PARSE_JSON: ClassVar["ObservabilityPipelineParseJSONProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineParseJSONProcessorType.PARSE_JSON = ObservabilityPipelineParseJSONProcessorType("parse_json")
