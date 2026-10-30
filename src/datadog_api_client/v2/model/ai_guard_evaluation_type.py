# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AIGuardEvaluationType(ModelSimple):
    """
    The JSON:API resource type for AI Guard evaluation requests and responses.
        Its value is `evaluations` for the action endpoint `/api/v2/ai-guard/evaluate`.

    :param value: If omitted defaults to "evaluations". Must be one of ["evaluations"].
    :type value: str
    """

    allowed_values = {
        "evaluations",
    }
    EVALUATIONS: ClassVar["AIGuardEvaluationType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AIGuardEvaluationType.EVALUATIONS = AIGuardEvaluationType("evaluations")
