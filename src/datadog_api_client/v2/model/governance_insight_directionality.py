# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class GovernanceInsightDirectionality(ModelSimple):
    """
    Whether an increase in the insight's value is good, bad, or neutral.

    :param value: Must be one of ["neutral", "increase_better", "decrease_better"].
    :type value: str
    """

    allowed_values = {
        "neutral",
        "increase_better",
        "decrease_better",
    }
    NEUTRAL: ClassVar["GovernanceInsightDirectionality"]
    INCREASE_BETTER: ClassVar["GovernanceInsightDirectionality"]
    DECREASE_BETTER: ClassVar["GovernanceInsightDirectionality"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


GovernanceInsightDirectionality.NEUTRAL = GovernanceInsightDirectionality("neutral")
GovernanceInsightDirectionality.INCREASE_BETTER = GovernanceInsightDirectionality("increase_better")
GovernanceInsightDirectionality.DECREASE_BETTER = GovernanceInsightDirectionality("decrease_better")
