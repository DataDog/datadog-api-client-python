# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceAccountType(ModelSimple):
    """
    Service account resource type.

    :param value: If omitted defaults to "service_account". Must be one of ["service_account"].
    :type value: str
    """

    allowed_values = {
        "service_account",
    }
    SERVICE_ACCOUNT: ClassVar["ServiceAccountType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceAccountType.SERVICE_ACCOUNT = ServiceAccountType("service_account")
