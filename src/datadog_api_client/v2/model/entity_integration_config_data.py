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
    from datadog_api_client.v2.model.entity_integration_config_attributes import EntityIntegrationConfigAttributes
    from datadog_api_client.v2.model.entity_integration_config_type import EntityIntegrationConfigType


class EntityIntegrationConfigData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_integration_config_attributes import EntityIntegrationConfigAttributes
        from datadog_api_client.v2.model.entity_integration_config_type import EntityIntegrationConfigType

        return {
            "attributes": (EntityIntegrationConfigAttributes,),
            "id": (str,),
            "type": (EntityIntegrationConfigType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: EntityIntegrationConfigAttributes, id: str, type: EntityIntegrationConfigType, **kwargs
    ):
        """
        JSON:API resource object for an entity integration configuration.

        :param attributes: The organization ID, integration identifier, and integration-specific configuration payload for an entity integration configuration.
        :type attributes: EntityIntegrationConfigAttributes

        :param id: Unique identifier of the entity integration configuration.
        :type id: str

        :param type: JSON:API resource type for an entity integration configuration. Always ``entity_integration_configs``.
        :type type: EntityIntegrationConfigType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
