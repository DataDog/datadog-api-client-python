# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SplitAPIKeyType(ModelSimple):
    """
    The definition of the `SplitAPIKey` object.

    :param value: If omitted defaults to "SplitAPIKey". Must be one of ["SplitAPIKey"].
    :type value: str
    """

    allowed_values = {
        "SplitAPIKey",
    }
    SPLITAPIKEY: ClassVar["SplitAPIKeyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SplitAPIKeyType.SPLITAPIKEY = SplitAPIKeyType("SplitAPIKey")
