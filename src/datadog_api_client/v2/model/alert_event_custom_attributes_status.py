# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AlertEventCustomAttributesStatus(ModelSimple):
    """
    The status of the alert.

    :param value: Must be one of ["warn", "error", "ok"].
    :type value: str
    """

    allowed_values = {
        "warn",
        "error",
        "ok",
    }
    WARN: ClassVar["AlertEventCustomAttributesStatus"]
    ERROR: ClassVar["AlertEventCustomAttributesStatus"]
    OK: ClassVar["AlertEventCustomAttributesStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AlertEventCustomAttributesStatus.WARN = AlertEventCustomAttributesStatus("warn")
AlertEventCustomAttributesStatus.ERROR = AlertEventCustomAttributesStatus("error")
AlertEventCustomAttributesStatus.OK = AlertEventCustomAttributesStatus("ok")
