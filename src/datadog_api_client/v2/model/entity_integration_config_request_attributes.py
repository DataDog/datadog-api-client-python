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


class EntityIntegrationConfigRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_integration_config_payload import EntityIntegrationConfigPayload

        return {
            "config": (EntityIntegrationConfigPayload,),
        }

    attribute_map = {
        "config": "config",
    }

    def __init__(self_, config: EntityIntegrationConfigPayload, **kwargs):
        """
        Attributes used to create or update an entity integration configuration.

        :param config: Integration-specific configuration payload. The shape of this object depends on the integration identified by the path parameter. For ``github`` , the object must contain an ``enabled_repos`` array. For ``jira`` , it must contain an ``enabled_projects`` array. For ``pagerduty`` , it must contain an ``accounts`` array.
        :type config: EntityIntegrationConfigPayload
        """
        super().__init__(kwargs)

        self_.config = config
