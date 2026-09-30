# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityContextEntityType(ModelSimple):
    """
    The type of entity to retrieve. Only `siem_entity_identity` is currently supported.

    :param value: If omitted defaults to "siem_entity_identity". Must be one of ["siem_entity_identity"].
    :type value: str
    """

    allowed_values = {
        "siem_entity_identity",
    }
    SIEM_ENTITY_IDENTITY: ClassVar["EntityContextEntityType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityContextEntityType.SIEM_ENTITY_IDENTITY = EntityContextEntityType("siem_entity_identity")
