# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_now_ticket_create_attributes import ServiceNowTicketCreateAttributes
    from datadog_api_client.v2.model.service_now_ticket_resource_type import ServiceNowTicketResourceType


class ServiceNowTicketCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_ticket_create_attributes import ServiceNowTicketCreateAttributes
        from datadog_api_client.v2.model.service_now_ticket_resource_type import ServiceNowTicketResourceType

        return {
            "attributes": (ServiceNowTicketCreateAttributes,),
            "type": (ServiceNowTicketResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: ServiceNowTicketCreateAttributes, type: ServiceNowTicketResourceType, **kwargs):
        """
        ServiceNow ticket creation data

        :param attributes: ServiceNow ticket creation attributes
        :type attributes: ServiceNowTicketCreateAttributes

        :param type: ServiceNow ticket resource type
        :type type: ServiceNowTicketResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
