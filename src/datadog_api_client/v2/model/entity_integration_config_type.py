# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityIntegrationConfigType(ModelSimple):
    """
    JSON:API resource type for an entity integration configuration. Always `entity_integration_configs`.

    :param value: If omitted defaults to "entity_integration_configs". Must be one of ["entity_integration_configs"].
    :type value: str
    """

    allowed_values = {
        "entity_integration_configs",
    }
    ENTITY_INTEGRATION_CONFIGS: ClassVar["EntityIntegrationConfigType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityIntegrationConfigType.ENTITY_INTEGRATION_CONFIGS = EntityIntegrationConfigType("entity_integration_configs")
