# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OwnershipSettingsType(ModelSimple):
    """
    The type of the ownership settings resource. The value should always be `ownership_settings`.

    :param value: If omitted defaults to "ownership_settings". Must be one of ["ownership_settings"].
    :type value: str
    """

    allowed_values = {
        "ownership_settings",
    }
    OWNERSHIP_SETTINGS: ClassVar["OwnershipSettingsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OwnershipSettingsType.OWNERSHIP_SETTINGS = OwnershipSettingsType("ownership_settings")
