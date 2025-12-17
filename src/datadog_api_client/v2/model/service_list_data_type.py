# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceListDataType(ModelSimple):
    """
    Services list resource type.

    :param value: If omitted defaults to "services_list". Must be one of ["services_list"].
    :type value: str
    """

    allowed_values = {
        "services_list",
    }
    SERVICES_LIST: ClassVar["ServiceListDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceListDataType.SERVICES_LIST = ServiceListDataType("services_list")
