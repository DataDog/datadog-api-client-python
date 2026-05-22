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
    from datadog_api_client.v2.model.entity_integration_config_request_data import EntityIntegrationConfigRequestData


class EntityIntegrationConfigRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_integration_config_request_data import (
            EntityIntegrationConfigRequestData,
        )

        return {
            "data": (EntityIntegrationConfigRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: EntityIntegrationConfigRequestData, **kwargs):
        """
        Request body used to create or replace the configuration for a given integration.

        :param data: JSON:API resource object used in a request to create or update an entity integration configuration.
        :type data: EntityIntegrationConfigRequestData
        """
        super().__init__(kwargs)

        self_.data = data
