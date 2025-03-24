# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityResponseIncludedRelatedEntityType(ModelSimple):
    """
    Related entity.

    :param value: If omitted defaults to "relatedEntity". Must be one of ["relatedEntity"].
    :type value: str
    """

    allowed_values = {
        "relatedEntity",
    }
    RELATED_ENTITY: ClassVar["EntityResponseIncludedRelatedEntityType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityResponseIncludedRelatedEntityType.RELATED_ENTITY = EntityResponseIncludedRelatedEntityType("relatedEntity")
