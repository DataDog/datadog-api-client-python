# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceAccessTokensType(ModelSimple):
    """
    Service access tokens resource type.

    :param value: If omitted defaults to "service_access_tokens". Must be one of ["service_access_tokens"].
    :type value: str
    """

    allowed_values = {
        "service_access_tokens",
    }
    SERVICE_ACCESS_TOKENS: ClassVar["ServiceAccessTokensType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceAccessTokensType.SERVICE_ACCESS_TOKENS = ServiceAccessTokensType("service_access_tokens")
