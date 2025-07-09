# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityV3APIVersion(ModelSimple):
    """
    The version of the schema data that was used to populate this entity's data. This could be via the API, Terraform, or YAML file in a repository. The field is known as schema-version in the previous version.

    :param value: Must be one of ["v3", "v2.2", "v2.1", "v2"].
    :type value: str
    """

    allowed_values = {
        "v3",
        "v2.2",
        "v2.1",
        "v2",
    }
    V3: ClassVar["EntityV3APIVersion"]
    V2_2: ClassVar["EntityV3APIVersion"]
    V2_1: ClassVar["EntityV3APIVersion"]
    V2: ClassVar["EntityV3APIVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityV3APIVersion.V3 = EntityV3APIVersion("v3")
EntityV3APIVersion.V2_2 = EntityV3APIVersion("v2.2")
EntityV3APIVersion.V2_1 = EntityV3APIVersion("v2.1")
EntityV3APIVersion.V2 = EntityV3APIVersion("v2")
