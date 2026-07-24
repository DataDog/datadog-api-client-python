# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentPageUUIDType(ModelSimple):
    """
    Resource type for a page UUID response.

    :param value: If omitted defaults to "page_uuid". Must be one of ["page_uuid"].
    :type value: str
    """

    allowed_values = {
        "page_uuid",
    }
    PAGE_UUID: ClassVar["IncidentPageUUIDType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentPageUUIDType.PAGE_UUID = IncidentPageUUIDType("page_uuid")
