# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FleetConfigFileSchemaV2ResourceType(ModelSimple):
    """
    The type of the configuration file schema resource.

    :param value: If omitted defaults to "config_file_schema". Must be one of ["config_file_schema"].
    :type value: str
    """

    allowed_values = {
        "config_file_schema",
    }
    CONFIG_FILE_SCHEMA: ClassVar["FleetConfigFileSchemaV2ResourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FleetConfigFileSchemaV2ResourceType.CONFIG_FILE_SCHEMA = FleetConfigFileSchemaV2ResourceType("config_file_schema")
