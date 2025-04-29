# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineEnrichmentTableFileKeyItemsComparison(ModelSimple):
    """
    Defines how to compare key fields for enrichment table lookups.

    :param value: If omitted defaults to "equals". Must be one of ["equals"].
    :type value: str
    """

    allowed_values = {
        "equals",
    }
    EQUALS: ClassVar["ObservabilityPipelineEnrichmentTableFileKeyItemsComparison"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineEnrichmentTableFileKeyItemsComparison.EQUALS = (
    ObservabilityPipelineEnrichmentTableFileKeyItemsComparison("equals")
)
