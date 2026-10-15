# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SavedFilterDataType(ModelSimple):
    """
    The saved filter resource type.

    :param value: If omitted defaults to "saved-filters". Must be one of ["saved-filters"].
    :type value: str
    """

    allowed_values = {
        "saved-filters",
    }
    SAVED_FILTERS: ClassVar["SavedFilterDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SavedFilterDataType.SAVED_FILTERS = SavedFilterDataType("saved-filters")
