# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceRepositoryInfoDataType(ModelSimple):
    """
    The resource type for service repository info objects.

    :param value: If omitted defaults to "service_repository_info". Must be one of ["service_repository_info"].
    :type value: str
    """

    allowed_values = {
        "service_repository_info",
    }
    SERVICE_REPOSITORY_INFO: ClassVar["ServiceRepositoryInfoDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceRepositoryInfoDataType.SERVICE_REPOSITORY_INFO = ServiceRepositoryInfoDataType("service_repository_info")
