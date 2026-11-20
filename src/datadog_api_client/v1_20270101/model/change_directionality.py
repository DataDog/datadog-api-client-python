# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeDirectionality(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["increase_better", "decrease_better", "neutral"].
    :type value: str
    """

    allowed_values = {
        "increase_better",
        "decrease_better",
        "neutral",
    }
    INCREASE_BETTER: ClassVar["ChangeDirectionality"]
    DECREASE_BETTER: ClassVar["ChangeDirectionality"]
    NEUTRAL: ClassVar["ChangeDirectionality"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeDirectionality.INCREASE_BETTER = ChangeDirectionality("increase_better")
ChangeDirectionality.DECREASE_BETTER = ChangeDirectionality("decrease_better")
ChangeDirectionality.NEUTRAL = ChangeDirectionality("neutral")
