# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineParseXMLProcessorType(ModelSimple):
    """
    The processor type. The value should always be `parse_xml`.

    :param value: If omitted defaults to "parse_xml". Must be one of ["parse_xml"].
    :type value: str
    """

    allowed_values = {
        "parse_xml",
    }
    PARSE_XML: ClassVar["ObservabilityPipelineParseXMLProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineParseXMLProcessorType.PARSE_XML = ObservabilityPipelineParseXMLProcessorType("parse_xml")
