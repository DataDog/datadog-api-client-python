# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsExperimentHoldoutV2DTODataType(ModelSimple):
    """
    Experiment holdout resource type.

    :param value: If omitted defaults to "experiment-holdouts". Must be one of ["experiment-holdouts"].
    :type value: str
    """

    allowed_values = {
        "experiment-holdouts",
    }
    EXPERIMENT_HOLDOUTS: ClassVar["ExperimentsExperimentHoldoutV2DTODataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsExperimentHoldoutV2DTODataType.EXPERIMENT_HOLDOUTS = ExperimentsExperimentHoldoutV2DTODataType(
    "experiment-holdouts"
)
