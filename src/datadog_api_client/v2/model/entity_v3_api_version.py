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
    The schema version of entity type. The field is known as schema-version in the previous version

    :param value: If omitted defaults to "v3". Must be one of ["v3"].
    :type value: str
    """

    allowed_values = {
        "v3",
    }
    V3: ClassVar["EntityV3APIVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityV3APIVersion.V3 = EntityV3APIVersion("v3")
