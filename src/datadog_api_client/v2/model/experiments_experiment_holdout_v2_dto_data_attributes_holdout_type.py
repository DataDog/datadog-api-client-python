# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType(ModelSimple):
    """
    How Datadog serves a MANAGED holdout. GLOBAL holdouts apply to every eligible experiment of a subject type. SELECTIVE holdouts apply only to the experiments attached to them. Null for EXTERNAL holdouts.

    :param value: Must be one of ["GLOBAL", "SELECTIVE", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "GLOBAL",
        "SELECTIVE",
        "UNKNOWN",
    }
    GLOBAL: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType"]
    SELECTIVE: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType"]
    UNKNOWN: ClassVar["ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType"]

    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType.GLOBAL = (
    ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType("GLOBAL")
)
ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType.SELECTIVE = (
    ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType("SELECTIVE")
)
ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType.UNKNOWN = (
    ExperimentsExperimentHoldoutV2DTODataAttributesHoldoutType("UNKNOWN")
)
