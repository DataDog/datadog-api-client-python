# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentV2DTODataAttributesConclusionOutcome(ModelSimple):
    """
    Recorded experiment outcome.

    :param value: Must be one of ["POSITIVE", "NEGATIVE", "NEUTRAL", "INCONCLUSIVE", "MISCONFIGURED", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "POSITIVE",
        "NEGATIVE",
        "NEUTRAL",
        "INCONCLUSIVE",
        "MISCONFIGURED",
        "UNKNOWN",
    }
    POSITIVE: ClassVar["ExperimentsExperimentV2DTODataAttributesConclusionOutcome"]
    NEGATIVE: ClassVar["ExperimentsExperimentV2DTODataAttributesConclusionOutcome"]
    NEUTRAL: ClassVar["ExperimentsExperimentV2DTODataAttributesConclusionOutcome"]
    INCONCLUSIVE: ClassVar["ExperimentsExperimentV2DTODataAttributesConclusionOutcome"]
    MISCONFIGURED: ClassVar["ExperimentsExperimentV2DTODataAttributesConclusionOutcome"]
    UNKNOWN: ClassVar["ExperimentsExperimentV2DTODataAttributesConclusionOutcome"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentV2DTODataAttributesConclusionOutcome.POSITIVE = (
    ExperimentsExperimentV2DTODataAttributesConclusionOutcome("POSITIVE")
)
ExperimentsExperimentV2DTODataAttributesConclusionOutcome.NEGATIVE = (
    ExperimentsExperimentV2DTODataAttributesConclusionOutcome("NEGATIVE")
)
ExperimentsExperimentV2DTODataAttributesConclusionOutcome.NEUTRAL = (
    ExperimentsExperimentV2DTODataAttributesConclusionOutcome("NEUTRAL")
)
ExperimentsExperimentV2DTODataAttributesConclusionOutcome.INCONCLUSIVE = (
    ExperimentsExperimentV2DTODataAttributesConclusionOutcome("INCONCLUSIVE")
)
ExperimentsExperimentV2DTODataAttributesConclusionOutcome.MISCONFIGURED = (
    ExperimentsExperimentV2DTODataAttributesConclusionOutcome("MISCONFIGURED")
)
ExperimentsExperimentV2DTODataAttributesConclusionOutcome.UNKNOWN = (
    ExperimentsExperimentV2DTODataAttributesConclusionOutcome("UNKNOWN")
)
