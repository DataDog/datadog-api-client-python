# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType(ModelSimple):
    """
    Kind of diagnostic check performed.

    :param value: Must be one of ["EXPERIMENT_HAS_ASSIGNMENTS", "METRIC_HAS_DATA", "ASSIGNMENT_IMBALANCE", "METRIC_WINSORIZE_ZERO", "PRE_EXPERIMENT_IMBALANCE", "MIXED_ASSIGNMENTS", "DIMENSIONAL_ASSIGNMENT_IMBALANCE", "FLAG_HAS_EVALUATIONS", "IMPLAUSIBLE_PRIOR", "DIMENSIONAL_DEGRADATION", "PIPELINE_STATUS", "MAPPED_ANALYSIS_CONFIGURATION", "MAPPED_ANALYSIS_COVERAGE", "MAPPED_ANALYSIS_COLLISIONS", "MAPPED_ANALYSIS_FANOUT", "MAPPED_ANALYSIS_CHANGE"].
    :type value: str
    """

    allowed_values = {
        "EXPERIMENT_HAS_ASSIGNMENTS",
        "METRIC_HAS_DATA",
        "ASSIGNMENT_IMBALANCE",
        "METRIC_WINSORIZE_ZERO",
        "PRE_EXPERIMENT_IMBALANCE",
        "MIXED_ASSIGNMENTS",
        "DIMENSIONAL_ASSIGNMENT_IMBALANCE",
        "FLAG_HAS_EVALUATIONS",
        "IMPLAUSIBLE_PRIOR",
        "DIMENSIONAL_DEGRADATION",
        "PIPELINE_STATUS",
        "MAPPED_ANALYSIS_CONFIGURATION",
        "MAPPED_ANALYSIS_COVERAGE",
        "MAPPED_ANALYSIS_COLLISIONS",
        "MAPPED_ANALYSIS_FANOUT",
        "MAPPED_ANALYSIS_CHANGE",
    }
    EXPERIMENT_HAS_ASSIGNMENTS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    METRIC_HAS_DATA: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    ASSIGNMENT_IMBALANCE: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    METRIC_WINSORIZE_ZERO: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    PRE_EXPERIMENT_IMBALANCE: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    MIXED_ASSIGNMENTS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    DIMENSIONAL_ASSIGNMENT_IMBALANCE: ClassVar[
        "ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"
    ]
    FLAG_HAS_EVALUATIONS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    IMPLAUSIBLE_PRIOR: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    DIMENSIONAL_DEGRADATION: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    PIPELINE_STATUS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    MAPPED_ANALYSIS_CONFIGURATION: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    MAPPED_ANALYSIS_COVERAGE: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    MAPPED_ANALYSIS_COLLISIONS: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    MAPPED_ANALYSIS_FANOUT: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]
    MAPPED_ANALYSIS_CHANGE: ClassVar["ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.EXPERIMENT_HAS_ASSIGNMENTS = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("EXPERIMENT_HAS_ASSIGNMENTS")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.METRIC_HAS_DATA = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("METRIC_HAS_DATA")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.ASSIGNMENT_IMBALANCE = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("ASSIGNMENT_IMBALANCE")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.METRIC_WINSORIZE_ZERO = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("METRIC_WINSORIZE_ZERO")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.PRE_EXPERIMENT_IMBALANCE = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("PRE_EXPERIMENT_IMBALANCE")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.MIXED_ASSIGNMENTS = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("MIXED_ASSIGNMENTS")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.DIMENSIONAL_ASSIGNMENT_IMBALANCE = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("DIMENSIONAL_ASSIGNMENT_IMBALANCE")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.FLAG_HAS_EVALUATIONS = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("FLAG_HAS_EVALUATIONS")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.IMPLAUSIBLE_PRIOR = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("IMPLAUSIBLE_PRIOR")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.DIMENSIONAL_DEGRADATION = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("DIMENSIONAL_DEGRADATION")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.PIPELINE_STATUS = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("PIPELINE_STATUS")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.MAPPED_ANALYSIS_CONFIGURATION = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("MAPPED_ANALYSIS_CONFIGURATION")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.MAPPED_ANALYSIS_COVERAGE = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("MAPPED_ANALYSIS_COVERAGE")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.MAPPED_ANALYSIS_COLLISIONS = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("MAPPED_ANALYSIS_COLLISIONS")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.MAPPED_ANALYSIS_FANOUT = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("MAPPED_ANALYSIS_FANOUT")
)
ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType.MAPPED_ANALYSIS_CHANGE = (
    ExperimentsExperimentDiagnosticsV2DTODataAttributesDiagnosticsItemsType("MAPPED_ANALYSIS_CHANGE")
)
