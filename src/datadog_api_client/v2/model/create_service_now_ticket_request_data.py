# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.create_service_now_ticket_request_data_attributes import (
        CreateServiceNowTicketRequestDataAttributes,
    )
    from datadog_api_client.v2.model.create_service_now_ticket_request_data_relationships import (
        CreateServiceNowTicketRequestDataRelationships,
    )
    from datadog_api_client.v2.model.service_now_tickets_data_type import ServiceNowTicketsDataType


class CreateServiceNowTicketRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_service_now_ticket_request_data_attributes import (
            CreateServiceNowTicketRequestDataAttributes,
        )
        from datadog_api_client.v2.model.create_service_now_ticket_request_data_relationships import (
            CreateServiceNowTicketRequestDataRelationships,
        )
        from datadog_api_client.v2.model.service_now_tickets_data_type import ServiceNowTicketsDataType

        return {
            "attributes": (CreateServiceNowTicketRequestDataAttributes,),
            "relationships": (CreateServiceNowTicketRequestDataRelationships,),
            "type": (ServiceNowTicketsDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        relationships: CreateServiceNowTicketRequestDataRelationships,
        type: ServiceNowTicketsDataType,
        attributes: Union[CreateServiceNowTicketRequestDataAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data of the ServiceNow ticket to create.

        :param attributes: Attributes of the ServiceNow ticket to create.
        :type attributes: CreateServiceNowTicketRequestDataAttributes, optional

        :param relationships: Relationships of the ServiceNow ticket to create.
        :type relationships: CreateServiceNowTicketRequestDataRelationships

        :param type: ServiceNow tickets resource type.
        :type type: ServiceNowTicketsDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.relationships = relationships
        self_.type = type
