# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason(ModelSimple):
    """
    Reason that the statistical result is marked as unreliable.

    :param value: Must be one of ["CONTROL_DENOMINATOR_NEAR_ZERO", "TREATMENT_DENOMINATOR_NEAR_ZERO", "CONTROL_AND_TREATMENT_DENOMINATORS_NEAR_ZERO", "CONTROL_MEAN_NEAR_ZERO", "ZERO_VARIANCE", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "CONTROL_DENOMINATOR_NEAR_ZERO",
        "TREATMENT_DENOMINATOR_NEAR_ZERO",
        "CONTROL_AND_TREATMENT_DENOMINATORS_NEAR_ZERO",
        "CONTROL_MEAN_NEAR_ZERO",
        "ZERO_VARIANCE",
        "UNKNOWN",
    }
    CONTROL_DENOMINATOR_NEAR_ZERO: ClassVar[
        "ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason"
    ]
    TREATMENT_DENOMINATOR_NEAR_ZERO: ClassVar[
        "ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason"
    ]
    CONTROL_AND_TREATMENT_DENOMINATORS_NEAR_ZERO: ClassVar[
        "ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason"
    ]
    CONTROL_MEAN_NEAR_ZERO: ClassVar[
        "ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason"
    ]
    ZERO_VARIANCE: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason"]
    UNKNOWN: ClassVar["ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason.CONTROL_DENOMINATOR_NEAR_ZERO = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason(
        "CONTROL_DENOMINATOR_NEAR_ZERO"
    )
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason.TREATMENT_DENOMINATOR_NEAR_ZERO = ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason(
    "TREATMENT_DENOMINATOR_NEAR_ZERO"
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason.CONTROL_AND_TREATMENT_DENOMINATORS_NEAR_ZERO = ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason(
    "CONTROL_AND_TREATMENT_DENOMINATORS_NEAR_ZERO"
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason.CONTROL_MEAN_NEAR_ZERO = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason("CONTROL_MEAN_NEAR_ZERO")
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason.ZERO_VARIANCE = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason("ZERO_VARIANCE")
)
ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason.UNKNOWN = (
    ExperimentsVariantResultsV2DTODataAttributesMetricsItemsAnalysesItemsUnreliableReason("UNKNOWN")
)
