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
    from datadog_api_client.v2.model.entity_integration_config_request_attributes import (
        EntityIntegrationConfigRequestAttributes,
    )
    from datadog_api_client.v2.model.entity_integration_config_request_type import EntityIntegrationConfigRequestType


class EntityIntegrationConfigRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_integration_config_request_attributes import (
            EntityIntegrationConfigRequestAttributes,
        )
        from datadog_api_client.v2.model.entity_integration_config_request_type import (
            EntityIntegrationConfigRequestType,
        )

        return {
            "attributes": (EntityIntegrationConfigRequestAttributes,),
            "type": (EntityIntegrationConfigRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: EntityIntegrationConfigRequestAttributes, type: EntityIntegrationConfigRequestType, **kwargs
    ):
        """
        JSON:API resource object used in a request to create or update an entity integration configuration.

        :param attributes: Attributes used to create or update an entity integration configuration.
        :type attributes: EntityIntegrationConfigRequestAttributes

        :param type: JSON:API resource type for the entity integration configuration create or update request. Always ``entity_integration_config_requests``.
        :type type: EntityIntegrationConfigRequestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
