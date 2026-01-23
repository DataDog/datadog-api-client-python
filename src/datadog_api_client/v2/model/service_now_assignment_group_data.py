# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.service_now_assignment_group_attributes import ServiceNowAssignmentGroupAttributes
    from datadog_api_client.v2.model.service_now_assignment_group_type import ServiceNowAssignmentGroupType


class ServiceNowAssignmentGroupData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_assignment_group_attributes import (
            ServiceNowAssignmentGroupAttributes,
        )
        from datadog_api_client.v2.model.service_now_assignment_group_type import ServiceNowAssignmentGroupType

        return {
            "attributes": (ServiceNowAssignmentGroupAttributes,),
            "id": (UUID,),
            "type": (ServiceNowAssignmentGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ServiceNowAssignmentGroupAttributes, id: UUID, type: ServiceNowAssignmentGroupType, **kwargs
    ):
        """
        Data object for a ServiceNow assignment group

        :param attributes: Attributes of a ServiceNow assignment group
        :type attributes: ServiceNowAssignmentGroupAttributes

        :param id: Unique identifier for the ServiceNow assignment group
        :type id: UUID

        :param type: Type identifier for ServiceNow assignment group resources
        :type type: ServiceNowAssignmentGroupType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
