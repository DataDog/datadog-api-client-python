# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ValidateAPIKeyStatus(ModelSimple):
    """
    Status of the validation. Always `ok` when both the API key and the application key are valid.

    :param value: If omitted defaults to "ok". Must be one of ["ok"].
    :type value: str
    """

    allowed_values = {
        "ok",
    }
    OK: ClassVar["ValidateAPIKeyStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ValidateAPIKeyStatus.OK = ValidateAPIKeyStatus("ok")
