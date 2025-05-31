# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineEnrichmentTableFileSchemaItemsType(ModelSimple):
    """
    Declares allowed data types for enrichment table columns.

    :param value: Must be one of ["string", "boolean", "integer", "float", "date", "timestamp"].
    :type value: str
    """

    allowed_values = {
        "string",
        "boolean",
        "integer",
        "float",
        "date",
        "timestamp",
    }
    STRING: ClassVar["ObservabilityPipelineEnrichmentTableFileSchemaItemsType"]
    BOOLEAN: ClassVar["ObservabilityPipelineEnrichmentTableFileSchemaItemsType"]
    INTEGER: ClassVar["ObservabilityPipelineEnrichmentTableFileSchemaItemsType"]
    FLOAT: ClassVar["ObservabilityPipelineEnrichmentTableFileSchemaItemsType"]
    DATE: ClassVar["ObservabilityPipelineEnrichmentTableFileSchemaItemsType"]
    TIMESTAMP: ClassVar["ObservabilityPipelineEnrichmentTableFileSchemaItemsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineEnrichmentTableFileSchemaItemsType.STRING = (
    ObservabilityPipelineEnrichmentTableFileSchemaItemsType("string")
)
ObservabilityPipelineEnrichmentTableFileSchemaItemsType.BOOLEAN = (
    ObservabilityPipelineEnrichmentTableFileSchemaItemsType("boolean")
)
ObservabilityPipelineEnrichmentTableFileSchemaItemsType.INTEGER = (
    ObservabilityPipelineEnrichmentTableFileSchemaItemsType("integer")
)
ObservabilityPipelineEnrichmentTableFileSchemaItemsType.FLOAT = ObservabilityPipelineEnrichmentTableFileSchemaItemsType(
    "float"
)
ObservabilityPipelineEnrichmentTableFileSchemaItemsType.DATE = ObservabilityPipelineEnrichmentTableFileSchemaItemsType(
    "date"
)
ObservabilityPipelineEnrichmentTableFileSchemaItemsType.TIMESTAMP = (
    ObservabilityPipelineEnrichmentTableFileSchemaItemsType("timestamp")
)
