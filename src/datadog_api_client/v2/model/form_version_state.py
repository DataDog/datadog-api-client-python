# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FormVersionState(ModelSimple):
    """
    The state of the form version.

    :param value: Must be one of ["draft", "frozen"].
    :type value: str
    """

    allowed_values = {
        "draft",
        "frozen",
    }
    DRAFT: ClassVar["FormVersionState"]
    FROZEN: ClassVar["FormVersionState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FormVersionState.DRAFT = FormVersionState("draft")
FormVersionState.FROZEN = FormVersionState("frozen")
