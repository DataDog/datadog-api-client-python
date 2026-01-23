# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceNowBusinessServiceType(ModelSimple):
    """
    Type identifier for ServiceNow business service resources

    :param value: If omitted defaults to "business_services". Must be one of ["business_services"].
    :type value: str
    """

    allowed_values = {
        "business_services",
    }
    BUSINESS_SERVICES: ClassVar["ServiceNowBusinessServiceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceNowBusinessServiceType.BUSINESS_SERVICES = ServiceNowBusinessServiceType("business_services")
