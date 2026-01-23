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
    from datadog_api_client.v2.model.service_now_user_attributes import ServiceNowUserAttributes
    from datadog_api_client.v2.model.service_now_user_type import ServiceNowUserType


class ServiceNowUserData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_now_user_attributes import ServiceNowUserAttributes
        from datadog_api_client.v2.model.service_now_user_type import ServiceNowUserType

        return {
            "attributes": (ServiceNowUserAttributes,),
            "id": (UUID,),
            "type": (ServiceNowUserType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ServiceNowUserAttributes, id: UUID, type: ServiceNowUserType, **kwargs):
        """
        Data object for a ServiceNow user

        :param attributes: Attributes of a ServiceNow user
        :type attributes: ServiceNowUserAttributes

        :param id: Unique identifier for the ServiceNow user
        :type id: UUID

        :param type: Type identifier for ServiceNow user resources
        :type type: ServiceNowUserType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
