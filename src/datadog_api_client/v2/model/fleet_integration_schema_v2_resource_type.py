# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetIntegrationSchemaV2ResourceType(ModelSimple):
    """
    The type of the integration schema resource.

    :param value: If omitted defaults to "integration_schema". Must be one of ["integration_schema"].
    :type value: str
    """

    allowed_values = {
        "integration_schema",
    }
    INTEGRATION_SCHEMA: ClassVar["FleetIntegrationSchemaV2ResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetIntegrationSchemaV2ResourceType.INTEGRATION_SCHEMA = FleetIntegrationSchemaV2ResourceType("integration_schema")
