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
    from datadog_api_client.v2.model.service_now_business_service_attributes import ServiceNowBusinessServiceAttributes
    from datadog_api_client.v2.model.service_now_business_service_type import ServiceNowBusinessServiceType


class ServiceNowBusinessServiceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_business_service_attributes import (
            ServiceNowBusinessServiceAttributes,
        )
        from datadog_api_client.v2.model.service_now_business_service_type import ServiceNowBusinessServiceType

        return {
            "attributes": (ServiceNowBusinessServiceAttributes,),
            "id": (UUID,),
            "type": (ServiceNowBusinessServiceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ServiceNowBusinessServiceAttributes, id: UUID, type: ServiceNowBusinessServiceType, **kwargs
    ):
        """
        Data object for a ServiceNow business service

        :param attributes: Attributes of a ServiceNow business service
        :type attributes: ServiceNowBusinessServiceAttributes

        :param id: Unique identifier for the ServiceNow business service
        :type id: UUID

        :param type: Type identifier for ServiceNow business service resources
        :type type: ServiceNowBusinessServiceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
