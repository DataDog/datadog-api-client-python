# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateAppResponseDataType(ModelSimple):
    """
    The definition of `CreateAppResponseDataType` object.

    :param value: If omitted defaults to "appDefinitions". Must be one of ["appDefinitions"].
    :type value: str
    """

    allowed_values = {
        "appDefinitions",
    }
    APPDEFINITIONS: ClassVar["CreateAppResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateAppResponseDataType.APPDEFINITIONS = CreateAppResponseDataType("appDefinitions")