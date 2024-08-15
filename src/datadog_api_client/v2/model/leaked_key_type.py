# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class LeakedKeyType(ModelSimple):
    """
    The definition of LeakedKeyType object.

    :param value: If omitted defaults to "leaked_keys". Must be one of ["leaked_keys"].
    :type value: str
    """

    allowed_values = {
        "leaked_keys",
    }
    LEAKED_KEYS: ClassVar["LeakedKeyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LeakedKeyType.LEAKED_KEYS = LeakedKeyType("leaked_keys")
