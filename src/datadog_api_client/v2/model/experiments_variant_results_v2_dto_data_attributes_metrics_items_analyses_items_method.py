# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod(ModelSimple):
    """
    Statistical method used to calculate this result.

    :param value: Must be one of ["FIXED_SAMPLE", "BAYESIAN", "SEQUENTIAL", "SEQUENTIAL_FIXED_HYBRID", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "FIXED_SAMPLE",
        "BAYESIAN",
        "SEQUENTIAL",
        "SEQUENTIAL_FIXED_HYBRID",
        "UNKNOWN",
    }
    FIXED_SAMPLE: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod"]
    BAYESIAN: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod"]
    SEQUENTIAL: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod"]
    SEQUENTIAL_FIXED_HYBRID: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod"]
    UNKNOWN: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod.FIXED_SAMPLE = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod("FIXED_SAMPLE")
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod.BAYESIAN = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod("BAYESIAN")
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod.SEQUENTIAL = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod("SEQUENTIAL")
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod.SEQUENTIAL_FIXED_HYBRID = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod("SEQUENTIAL_FIXED_HYBRID")
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod.UNKNOWN = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsMethod("UNKNOWN")
)
