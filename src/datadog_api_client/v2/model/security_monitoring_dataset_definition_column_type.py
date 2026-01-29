# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringDatasetDefinitionColumnType(ModelSimple):
    """
    The type of the column in a dataset definition.

    :param value: Must be one of ["string", "integer", "double", "boolean"].
    :type value: str
    """

    allowed_values = {
        "string",
        "integer",
        "double",
        "boolean",
    }
    STRING: ClassVar["SecurityMonitoringDatasetDefinitionColumnType"]
    INTEGER: ClassVar["SecurityMonitoringDatasetDefinitionColumnType"]
    DOUBLE: ClassVar["SecurityMonitoringDatasetDefinitionColumnType"]
    BOOLEAN: ClassVar["SecurityMonitoringDatasetDefinitionColumnType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringDatasetDefinitionColumnType.STRING = SecurityMonitoringDatasetDefinitionColumnType("string")
SecurityMonitoringDatasetDefinitionColumnType.INTEGER = SecurityMonitoringDatasetDefinitionColumnType("integer")
SecurityMonitoringDatasetDefinitionColumnType.DOUBLE = SecurityMonitoringDatasetDefinitionColumnType("double")
SecurityMonitoringDatasetDefinitionColumnType.BOOLEAN = SecurityMonitoringDatasetDefinitionColumnType("boolean")
