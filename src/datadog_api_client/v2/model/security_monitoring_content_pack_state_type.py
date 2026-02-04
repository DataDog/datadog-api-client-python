# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringContentPackStateType(ModelSimple):
    """
    Type for content pack state object

    :param value: If omitted defaults to "content_pack_state". Must be one of ["content_pack_state"].
    :type value: str
    """

    allowed_values = {
        "content_pack_state",
    }
    CONTENT_PACK_STATE: ClassVar["SecurityMonitoringContentPackStateType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringContentPackStateType.CONTENT_PACK_STATE = SecurityMonitoringContentPackStateType("content_pack_state")
