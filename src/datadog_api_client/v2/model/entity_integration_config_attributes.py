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
    from datadog_api_client.v2.model.entity_integration_config_payload import EntityIntegrationConfigPayload


class EntityIntegrationConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_integration_config_payload import EntityIntegrationConfigPayload

        return {
            "config": (EntityIntegrationConfigPayload,),
            "integration_id": (str,),
            "org_id": (int,),
        }

    attribute_map = {
        "config": "config",
        "integration_id": "integration_id",
        "org_id": "org_id",
    }

    def __init__(self_, config: EntityIntegrationConfigPayload, integration_id: str, org_id: int, **kwargs):
        """
        The organization ID, integration identifier, and integration-specific configuration payload for an entity integration configuration.

        :param config: Integration-specific configuration payload. The shape of this object depends on the integration identified by the path parameter. For ``github`` , the object must contain an ``enabled_repos`` array. For ``jira`` , it must contain an ``enabled_projects`` array. For ``pagerduty`` , it must contain an ``accounts`` array.
        :type config: EntityIntegrationConfigPayload

        :param integration_id: The identifier of the integration this configuration applies to (for example, ``github`` , ``jira`` , or ``pagerduty`` ).
        :type integration_id: str

        :param org_id: The Datadog organization identifier that owns this configuration.
        :type org_id: int
        """
        super().__init__(kwargs)

        self_.config = config
        self_.integration_id = integration_id
        self_.org_id = org_id
