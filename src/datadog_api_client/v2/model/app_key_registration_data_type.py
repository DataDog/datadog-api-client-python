# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppKeyRegistrationDataType(ModelSimple):
    """
    The definition of `AppKeyRegistrationDataType` object.

    :param value: If omitted defaults to "app_key_registration". Must be one of ["app_key_registration"].
    :type value: str
    """

    allowed_values = {
        "app_key_registration",
    }
    APP_KEY_REGISTRATION: ClassVar["AppKeyRegistrationDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppKeyRegistrationDataType.APP_KEY_REGISTRATION = AppKeyRegistrationDataType("app_key_registration")
