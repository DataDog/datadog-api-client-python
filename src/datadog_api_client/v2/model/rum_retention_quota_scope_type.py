# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionQuotaScopeType(ModelSimple):
    """
    The type of scope the retention quota configuration applies to.

    :param value: If omitted defaults to "application". Must be one of ["application"].
    :type value: str
    """

    allowed_values = {
        "application",
    }
    APPLICATION: ClassVar["RumRetentionQuotaScopeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionQuotaScopeType.APPLICATION = RumRetentionQuotaScopeType("application")
