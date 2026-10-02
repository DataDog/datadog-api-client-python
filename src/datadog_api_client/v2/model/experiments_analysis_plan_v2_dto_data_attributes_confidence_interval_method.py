# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod(ModelSimple):
    """
    Statistical method used to calculate the experiment results.

    :param value: Must be one of ["Sequential", "FixedSample", "Bayesian", "SequentialFixedHybrid"].
    :type value: str
    """

    allowed_values = {
        "Sequential",
        "FixedSample",
        "Bayesian",
        "SequentialFixedHybrid",
    }
    SEQUENTIAL: ClassVar["ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod"]
    FIXEDSAMPLE: ClassVar["ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod"]
    BAYESIAN: ClassVar["ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod"]
    SEQUENTIALFIXEDHYBRID: ClassVar["ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod.SEQUENTIAL = (
    ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod("Sequential")
)
ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod.FIXEDSAMPLE = (
    ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod("FixedSample")
)
ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod.BAYESIAN = (
    ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod("Bayesian")
)
ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod.SEQUENTIALFIXEDHYBRID = (
    ExperimentsAnalysisPlanV2DTODataAttributesConfidenceIntervalMethod("SequentialFixedHybrid")
)
