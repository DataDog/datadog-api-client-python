# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ListServiceAccountApplicationKeysInclude(ModelSimple):
    """
    The definition of ListServiceAccountApplicationKeysInclude object.

    :param value: Must be one of ["leak_information", "owned_by"].
    :type value: str
    """

    allowed_values = {
        "leak_information",
        "owned_by",
    }
    LEAK_INFORMATION: ClassVar["ListServiceAccountApplicationKeysInclude"]
    OWNED_BY: ClassVar["ListServiceAccountApplicationKeysInclude"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ListServiceAccountApplicationKeysInclude.LEAK_INFORMATION = ListServiceAccountApplicationKeysInclude("leak_information")
ListServiceAccountApplicationKeysInclude.OWNED_BY = ListServiceAccountApplicationKeysInclude("owned_by")
