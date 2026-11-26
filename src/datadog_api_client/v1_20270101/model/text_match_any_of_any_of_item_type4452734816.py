# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TextMatchAnyOfAnyOfItemType4452734816(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "does_not_contain". Must be one of ["does_not_contain"].
    :type value: str
    """

    allowed_values = {
        "does_not_contain",
    }
    DOES_NOT_CONTAIN: ClassVar["TextMatchAnyOfAnyOfItemType4452734816"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TextMatchAnyOfAnyOfItemType4452734816.DOES_NOT_CONTAIN = TextMatchAnyOfAnyOfItemType4452734816("does_not_contain")
