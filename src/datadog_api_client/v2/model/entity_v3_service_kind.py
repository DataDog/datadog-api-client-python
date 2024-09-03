# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityV3ServiceKind(ModelSimple):
    """
    The definition of Entity V3 Service Kind object.

    :param value: If omitted defaults to "service". Must be one of ["service"].
    :type value: str
    """

    allowed_values = {
        "service",
    }
    SERVICE: ClassVar["EntityV3ServiceKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityV3ServiceKind.SERVICE = EntityV3ServiceKind("service")
