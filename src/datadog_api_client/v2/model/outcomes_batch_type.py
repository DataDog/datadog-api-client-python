# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OutcomesBatchType(ModelSimple):
    """
    The JSON:API type for scorecard outcomes.

    :param value: If omitted defaults to "batched-outcome". Must be one of ["batched-outcome"].
    :type value: str
    """

    allowed_values = {
        "batched-outcome",
    }
    BATCHED_OUTCOME: ClassVar["OutcomesBatchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OutcomesBatchType.BATCHED_OUTCOME = OutcomesBatchType("batched-outcome")
