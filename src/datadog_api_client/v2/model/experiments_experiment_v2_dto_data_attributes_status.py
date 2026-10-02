# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentV2DTODataAttributesStatus(ModelSimple):
    """
    Current stage in the experiment lifecycle.

    :param value: Must be one of ["DRAFT", "SCHEDULED", "IN_PROGRESS", "READY_FOR_DECISION", "DECISION_MADE", "CANCELLED", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "DRAFT",
        "SCHEDULED",
        "IN_PROGRESS",
        "READY_FOR_DECISION",
        "DECISION_MADE",
        "CANCELLED",
        "UNKNOWN",
    }
    DRAFT: ClassVar["ExperimentsExperimentV2DTODataAttributesStatus"]
    SCHEDULED: ClassVar["ExperimentsExperimentV2DTODataAttributesStatus"]
    IN_PROGRESS: ClassVar["ExperimentsExperimentV2DTODataAttributesStatus"]
    READY_FOR_DECISION: ClassVar["ExperimentsExperimentV2DTODataAttributesStatus"]
    DECISION_MADE: ClassVar["ExperimentsExperimentV2DTODataAttributesStatus"]
    CANCELLED: ClassVar["ExperimentsExperimentV2DTODataAttributesStatus"]
    UNKNOWN: ClassVar["ExperimentsExperimentV2DTODataAttributesStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentV2DTODataAttributesStatus.DRAFT = ExperimentsExperimentV2DTODataAttributesStatus("DRAFT")
ExperimentsExperimentV2DTODataAttributesStatus.SCHEDULED = ExperimentsExperimentV2DTODataAttributesStatus("SCHEDULED")
ExperimentsExperimentV2DTODataAttributesStatus.IN_PROGRESS = ExperimentsExperimentV2DTODataAttributesStatus(
    "IN_PROGRESS"
)
ExperimentsExperimentV2DTODataAttributesStatus.READY_FOR_DECISION = ExperimentsExperimentV2DTODataAttributesStatus(
    "READY_FOR_DECISION"
)
ExperimentsExperimentV2DTODataAttributesStatus.DECISION_MADE = ExperimentsExperimentV2DTODataAttributesStatus(
    "DECISION_MADE"
)
ExperimentsExperimentV2DTODataAttributesStatus.CANCELLED = ExperimentsExperimentV2DTODataAttributesStatus("CANCELLED")
ExperimentsExperimentV2DTODataAttributesStatus.UNKNOWN = ExperimentsExperimentV2DTODataAttributesStatus("UNKNOWN")
