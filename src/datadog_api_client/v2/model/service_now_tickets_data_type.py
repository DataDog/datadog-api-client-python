# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceNowTicketsDataType(ModelSimple):
    """
    ServiceNow tickets resource type.

    :param value: If omitted defaults to "servicenow_tickets". Must be one of ["servicenow_tickets"].
    :type value: str
    """

    allowed_values = {
        "servicenow_tickets",
    }
    SERVICENOW_TICKETS: ClassVar["ServiceNowTicketsDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceNowTicketsDataType.SERVICENOW_TICKETS = ServiceNowTicketsDataType("servicenow_tickets")
