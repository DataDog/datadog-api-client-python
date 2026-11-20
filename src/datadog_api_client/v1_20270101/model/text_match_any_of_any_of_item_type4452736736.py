# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TextMatchAnyOfAnyOfItemType4452736736(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "ends_with". Must be one of ["ends_with"].
    :type value: str
    """

    allowed_values = {
        "ends_with",
    }
    ENDS_WITH: ClassVar["TextMatchAnyOfAnyOfItemType4452736736"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TextMatchAnyOfAnyOfItemType4452736736.ENDS_WITH = TextMatchAnyOfAnyOfItemType4452736736("ends_with")
