# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DORAFailureType(ModelSimple):
    """
    JSON:API type for DORA failure events.

    :param value: If omitted defaults to "dora_failure". Must be one of ["dora_failure"].
    :type value: str
    """

    allowed_values = {
        "dora_failure",
    }
    DORA_FAILURE: ClassVar["DORAFailureType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DORAFailureType.DORA_FAILURE = DORAFailureType("dora_failure")
