# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsExperimentEventsType(ModelSimple):
    """
    Resource type for an experiment events collection.

    :param value: If omitted defaults to "experiment_events". Must be one of ["experiment_events"].
    :type value: str
    """

    allowed_values = {
        "experiment_events",
    }
    EXPERIMENT_EVENTS: ClassVar["LLMObsExperimentEventsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsExperimentEventsType.EXPERIMENT_EVENTS = LLMObsExperimentEventsType("experiment_events")
