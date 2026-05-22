# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityIntegrationConfigRequestType(ModelSimple):
    """
    JSON:API resource type for the entity integration configuration create or update request. Always `entity_integration_config_requests`.

    :param value: If omitted defaults to "entity_integration_config_requests". Must be one of ["entity_integration_config_requests"].
    :type value: str
    """

    allowed_values = {
        "entity_integration_config_requests",
    }
    ENTITY_INTEGRATION_CONFIG_REQUESTS: ClassVar["EntityIntegrationConfigRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityIntegrationConfigRequestType.ENTITY_INTEGRATION_CONFIG_REQUESTS = EntityIntegrationConfigRequestType(
    "entity_integration_config_requests"
)
