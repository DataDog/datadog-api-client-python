# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CIAppTestLevel(ModelSimple):
    """
    Test run level.

    :param value: Must be one of ["session", "module", "suite", "test"].
    :type value: str
    """

    allowed_values = {
        "session",
        "module",
        "suite",
        "test",
    }
    SESSION: ClassVar["CIAppTestLevel"]
    MODULE: ClassVar["CIAppTestLevel"]
    SUITE: ClassVar["CIAppTestLevel"]
    TEST: ClassVar["CIAppTestLevel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CIAppTestLevel.SESSION = CIAppTestLevel("session")
CIAppTestLevel.MODULE = CIAppTestLevel("module")
CIAppTestLevel.SUITE = CIAppTestLevel("suite")
CIAppTestLevel.TEST = CIAppTestLevel("test")
