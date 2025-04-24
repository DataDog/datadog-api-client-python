# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineEnrichmentTableProcessorType(ModelSimple):
    """
    The processor type. The value should always be `enrichment_table`.

    :param value: If omitted defaults to "enrichment_table". Must be one of ["enrichment_table"].
    :type value: str
    """

    allowed_values = {
        "enrichment_table",
    }
    ENRICHMENT_TABLE: ClassVar["ObservabilityPipelineEnrichmentTableProcessorType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineEnrichmentTableProcessorType.ENRICHMENT_TABLE = ObservabilityPipelineEnrichmentTableProcessorType(
    "enrichment_table"
)
