# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ApplicationSecurityServiceType(ModelSimple):
    """
    The type of the resource. The value should always be `service_env`.

    :param value: If omitted defaults to "service_env". Must be one of ["service_env"].
    :type value: str
    """

    allowed_values = {
        "service_env",
    }
    SERVICE_ENV: ClassVar["ApplicationSecurityServiceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ApplicationSecurityServiceType.SERVICE_ENV = ApplicationSecurityServiceType("service_env")
