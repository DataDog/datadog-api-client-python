# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentDiagnosticsV2DTODataAttributesState(ModelSimple):
    """
    Current state of the diagnostic evaluation.

    :param value: Must be one of ["NOT_STARTED", "RUNNING", "COMPLETED", "FAILED"].
    :type value: str
    """

    allowed_values = {
        "NOT_STARTED",
        "RUNNING",
        "COMPLETED",
        "FAILED",
    }
    NOT_STARTED: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesState"]
    RUNNING: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesState"]
    COMPLETED: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesState"]
    FAILED: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentDiagnosticsV2DTODataAttributesState.NOT_STARTED = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesState("NOT_STARTED")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesState.RUNNING = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesState("RUNNING")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesState.COMPLETED = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesState("COMPLETED")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesState.FAILED = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesState("FAILED")
)
