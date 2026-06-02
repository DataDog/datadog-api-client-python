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
    from datadog_api_client.v2.model.attach_service_now_ticket_request_data_attributes import (
        AttachServiceNowTicketRequestDataAttributes,
    )
    from datadog_api_client.v2.model.attach_service_now_ticket_request_data_relationships import (
        AttachServiceNowTicketRequestDataRelationships,
    )
    from datadog_api_client.v2.model.service_now_tickets_data_type import ServiceNowTicketsDataType


class AttachServiceNowTicketRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attach_service_now_ticket_request_data_attributes import (
            AttachServiceNowTicketRequestDataAttributes,
        )
        from datadog_api_client.v2.model.attach_service_now_ticket_request_data_relationships import (
            AttachServiceNowTicketRequestDataRelationships,
        )
        from datadog_api_client.v2.model.service_now_tickets_data_type import ServiceNowTicketsDataType

        return {
            "attributes": (AttachServiceNowTicketRequestDataAttributes,),
            "relationships": (AttachServiceNowTicketRequestDataRelationships,),
            "type": (ServiceNowTicketsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AttachServiceNowTicketRequestDataAttributes,
        relationships: AttachServiceNowTicketRequestDataRelationships,
        type: ServiceNowTicketsDataType,
        **kwargs,
    ):
        """
        Data of the ServiceNow ticket to attach security findings to.

        :param attributes: Attributes of the ServiceNow ticket to attach security findings to.
        :type attributes: AttachServiceNowTicketRequestDataAttributes

        :param relationships: Relationships of the ServiceNow ticket to attach security findings to.
        :type relationships: AttachServiceNowTicketRequestDataRelationships

        :param type: ServiceNow tickets resource type.
        :type type: ServiceNowTicketsDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
