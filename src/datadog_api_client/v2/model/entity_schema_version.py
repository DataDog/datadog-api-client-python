# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntitySchemaVersion(ModelSimple):
    """
    Entity schema version for conversion.

    :param value: Must be one of ["v2", "v2.1", "v2.2", "v3"].
    :type value: str
    """

    allowed_values = {
        "v2",
        "v2.1",
        "v2.2",
        "v3",
    }
    V2: ClassVar["EntitySchemaVersion"]
    V2_1: ClassVar["EntitySchemaVersion"]
    V2_2: ClassVar["EntitySchemaVersion"]
    V3: ClassVar["EntitySchemaVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntitySchemaVersion.V2 = EntitySchemaVersion("v2")
EntitySchemaVersion.V2_1 = EntitySchemaVersion("v2.1")
EntitySchemaVersion.V2_2 = EntitySchemaVersion("v2.2")
EntitySchemaVersion.V3 = EntitySchemaVersion("v3")
