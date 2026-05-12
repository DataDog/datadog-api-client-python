# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ValidateV2Type(ModelSimple):
    """
    Resource type for the API key validation response.

    :param value: If omitted defaults to "validate_v2". Must be one of ["validate_v2"].
    :type value: str
    """

    allowed_values = {
        "validate_v2",
    }
    ValidateV2: ClassVar["ValidateV2Type"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ValidateV2Type.ValidateV2 = ValidateV2Type("validate_v2")
