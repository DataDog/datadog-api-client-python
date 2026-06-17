# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IntakeAPIKeyType(ModelSimple):
    """
    The resource type for an intake API key.

    :param value: If omitted defaults to "intake_api_key". Must be one of ["intake_api_key"].
    :type value: str
    """

    allowed_values = {
        "intake_api_key",
    }
    INTAKE_API_KEY: ClassVar["IntakeAPIKeyType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IntakeAPIKeyType.INTAKE_API_KEY = IntakeAPIKeyType("intake_api_key")
