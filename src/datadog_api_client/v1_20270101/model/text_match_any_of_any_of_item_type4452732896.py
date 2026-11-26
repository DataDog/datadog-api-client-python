# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TextMatchAnyOfAnyOfItemType4452732896(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "is_not". Must be one of ["is_not"].
    :type value: str
    """

    allowed_values = {
        "is_not",
    }
    IS_NOT: ClassVar["TextMatchAnyOfAnyOfItemType4452732896"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TextMatchAnyOfAnyOfItemType4452732896.IS_NOT = TextMatchAnyOfAnyOfItemType4452732896("is_not")
