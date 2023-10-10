# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ServiceDefinitionSchemaVersions(ModelSimple):
    """
    Schema versions

    :param value: Must be one of ["v1", "v2", "v2.1", "v2.2"].
    :type value: str
    """

    allowed_values = {
        "v1",
        "v2",
        "v2.1",
        "v2.2",
    }
    V1: ClassVar["ServiceDefinitionSchemaVersions"]
    V2: ClassVar["ServiceDefinitionSchemaVersions"]
    V2_1: ClassVar["ServiceDefinitionSchemaVersions"]
    V2_2: ClassVar["ServiceDefinitionSchemaVersions"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ServiceDefinitionSchemaVersions.V1 = ServiceDefinitionSchemaVersions("v1")
ServiceDefinitionSchemaVersions.V2 = ServiceDefinitionSchemaVersions("v2")
ServiceDefinitionSchemaVersions.V2_1 = ServiceDefinitionSchemaVersions("v2.1")
ServiceDefinitionSchemaVersions.V2_2 = ServiceDefinitionSchemaVersions("v2.2")
