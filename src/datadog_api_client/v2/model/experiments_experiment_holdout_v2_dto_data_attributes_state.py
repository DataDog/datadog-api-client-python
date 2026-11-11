# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentHoldoutV2DTODataAttributesState(ModelSimple):
    """
    Lifecycle phase of the holdout. PENDING holdouts have not started including experiments. INCLUDING holdouts are adding experiments. WAITING_FOR_ANALYSIS holdouts have stopped including experiments but have not started analysis. ANALYSING holdouts are in their analysis window. COMPLETE applies only to EXTERNAL holdouts that have ended their analysis window but are not archived.

    :param value: Must be one of ["PENDING", "INCLUDING", "WAITING_FOR_ANALYSIS", "ANALYSING", "COMPLETE", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "PENDING",
        "INCLUDING",
        "WAITING_FOR_ANALYSIS",
        "ANALYSING",
        "COMPLETE",
        "UNKNOWN",
    }
    PENDING: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesState"]
    INCLUDING: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesState"]
    WAITING_FOR_ANALYSIS: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesState"]
    ANALYSING: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesState"]
    COMPLETE: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesState"]
    UNKNOWN: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentHoldoutV2DTODataAttributesState.PENDING = ExperimentsExperimentHoldoutV2DTODataAttributesState(
    "PENDING"
)
ExperimentsExperimentHoldoutV2DTODataAttributesState.INCLUDING = ExperimentsExperimentHoldoutV2DTODataAttributesState(
    "INCLUDING"
)
ExperimentsExperimentHoldoutV2DTODataAttributesState.WAITING_FOR_ANALYSIS = (
    ExperimentsExperimentHoldoutV2DTODataAttributesState("WAITING_FOR_ANALYSIS")
)
ExperimentsExperimentHoldoutV2DTODataAttributesState.ANALYSING = ExperimentsExperimentHoldoutV2DTODataAttributesState(
    "ANALYSING"
)
ExperimentsExperimentHoldoutV2DTODataAttributesState.COMPLETE = ExperimentsExperimentHoldoutV2DTODataAttributesState(
    "COMPLETE"
)
ExperimentsExperimentHoldoutV2DTODataAttributesState.UNKNOWN = ExperimentsExperimentHoldoutV2DTODataAttributesState(
    "UNKNOWN"
)
