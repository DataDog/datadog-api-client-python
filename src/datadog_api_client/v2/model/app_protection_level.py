# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppProtectionLevel(ModelSimple):
    """
    The publication protection level of the app. `approval_required` means changes must go through an approval workflow before being published.

    :param value: Must be one of ["direct_publish", "approval_required"].
    :type value: str
    """

    allowed_values = {
        "direct_publish",
        "approval_required",
    }
    DIRECT_PUBLISH: ClassVar["AppProtectionLevel"]
    APPROVAL_REQUIRED: ClassVar["AppProtectionLevel"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppProtectionLevel.DIRECT_PUBLISH = AppProtectionLevel("direct_publish")
AppProtectionLevel.APPROVAL_REQUIRED = AppProtectionLevel("approval_required")
