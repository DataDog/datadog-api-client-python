# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityV3SystemKind(ModelSimple):
    """
    The definition of Entity V3 System Kind object.

    :param value: If omitted defaults to "system". Must be one of ["system"].
    :type value: str
    """

    allowed_values = {
        "system",
    }
    SYSTEM: ClassVar["EntityV3SystemKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityV3SystemKind.SYSTEM = EntityV3SystemKind("system")
