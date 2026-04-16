# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IoCScoreEffect(ModelSimple):
    """
    Effect of a scoring factor on the indicator's threat score.

    :param value: Must be one of ["RAISE_SCORE", "LOWER_SCORE", "NO_EFFECT"].
    :type value: str
    """

    allowed_values = {
        "RAISE_SCORE",
        "LOWER_SCORE",
        "NO_EFFECT",
    }
    RAISE_SCORE: ClassVar["IoCScoreEffect"]
    LOWER_SCORE: ClassVar["IoCScoreEffect"]
    NO_EFFECT: ClassVar["IoCScoreEffect"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IoCScoreEffect.RAISE_SCORE = IoCScoreEffect("RAISE_SCORE")
IoCScoreEffect.LOWER_SCORE = IoCScoreEffect("LOWER_SCORE")
IoCScoreEffect.NO_EFFECT = IoCScoreEffect("NO_EFFECT")
