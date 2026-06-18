# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class VercelConfigDataResponseType(ModelSimple):
    """
    Type identifier for a Vercel configuration resource.

    :param value: If omitted defaults to "vercelConfiguration". Must be one of ["vercelConfiguration"].
    :type value: str
    """

    allowed_values = {
        "vercelConfiguration",
    }
    VERCEL_CONFIGURATION: ClassVar["VercelConfigDataResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


VercelConfigDataResponseType.VERCEL_CONFIGURATION = VercelConfigDataResponseType("vercelConfiguration")
