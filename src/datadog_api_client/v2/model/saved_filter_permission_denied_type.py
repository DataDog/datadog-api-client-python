# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SavedFilterPermissionDeniedType(ModelSimple):
    """
    The resource type for this saved filter update error.

    :param value: If omitted defaults to "update-grace-denied". Must be one of ["update-grace-denied"].
    :type value: str
    """

    allowed_values = {
        "update-grace-denied",
    }
    UPDATE_GRACE_DENIED: ClassVar["SavedFilterPermissionDeniedType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SavedFilterPermissionDeniedType.UPDATE_GRACE_DENIED = SavedFilterPermissionDeniedType("update-grace-denied")
