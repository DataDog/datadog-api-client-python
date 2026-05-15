# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppVersionType(ModelSimple):
    """
    The app-version resource type.

    :param value: If omitted defaults to "appVersions". Must be one of ["appVersions"].
    :type value: str
    """

    allowed_values = {
        "appVersions",
    }
    APPVERSIONS: ClassVar["AppVersionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppVersionType.APPVERSIONS = AppVersionType("appVersions")
