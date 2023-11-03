# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class State(ModelSimple):
    """
    The state of the rule evaluation.

    :param value: Must be one of ["pass", "fail", "skip"].
    :type value: str
    """

    allowed_values = {
        "pass",
        "fail",
        "skip",
    }
    PASS: ClassVar["State"]
    FAIL: ClassVar["State"]
    SKIP: ClassVar["State"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


State.PASS = State("pass")
State.FAIL = State("fail")
State.SKIP = State("skip")
