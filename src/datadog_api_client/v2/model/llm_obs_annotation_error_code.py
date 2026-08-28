# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LLMObsAnnotationErrorCode(ModelSimple):
    """
    Stable error code. `permission_denied` indicates the item was rejected by queue access rules.

    :param value: If omitted defaults to "permission_denied". Must be one of ["permission_denied"].
    :type value: str
    """

    allowed_values = {
        "permission_denied",
    }
    PERMISSION_DENIED: ClassVar["LLMObsAnnotationErrorCode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LLMObsAnnotationErrorCode.PERMISSION_DENIED = LLMObsAnnotationErrorCode("permission_denied")
