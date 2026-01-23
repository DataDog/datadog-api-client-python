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
    from datadog_api_client.v2.model.service_now_instance_attributes import ServiceNowInstanceAttributes
    from datadog_api_client.v2.model.service_now_instance_type import ServiceNowInstanceType


class ServiceNowInstanceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_instance_attributes import ServiceNowInstanceAttributes
        from datadog_api_client.v2.model.service_now_instance_type import ServiceNowInstanceType

        return {
            "attributes": (ServiceNowInstanceAttributes,),
            "id": (UUID,),
            "type": (ServiceNowInstanceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ServiceNowInstanceAttributes, id: UUID, type: ServiceNowInstanceType, **kwargs):
        """
        Data object for a ServiceNow instance

        :param attributes: Attributes of a ServiceNow instance
        :type attributes: ServiceNowInstanceAttributes

        :param id: Unique identifier for the ServiceNow instance
        :type id: UUID

        :param type: Type identifier for ServiceNow instance resources
        :type type: ServiceNowInstanceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
