# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FindingEvaluation(ModelSimple):
    """
    The evaluation of the finding.

    :param value: Must be one of ["pass", "fail"].
    :type value: str
    """

    allowed_values = {
        "pass",
        "fail",
    }
    PASS: ClassVar["FindingEvaluation"]
    FAIL: ClassVar["FindingEvaluation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FindingEvaluation.PASS = FindingEvaluation("pass")
FindingEvaluation.FAIL = FindingEvaluation("fail")
