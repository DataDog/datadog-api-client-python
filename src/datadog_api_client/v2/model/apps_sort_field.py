# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AppsSortField(ModelSimple):
    """
    The field and direction to sort apps by

    :param value: Must be one of ["name", "created_at", "updated_at", "user_name", "-name", "-created_at", "-updated_at", "-user_name"].
    :type value: str
    """

    allowed_values = {
        "name",
        "created_at",
        "updated_at",
        "user_name",
        "-name",
        "-created_at",
        "-updated_at",
        "-user_name",
    }
    NAME: ClassVar["AppsSortField"]
    CREATED_AT: ClassVar["AppsSortField"]
    UPDATED_AT: ClassVar["AppsSortField"]
    USER_NAME: ClassVar["AppsSortField"]
    NAME_DESC: ClassVar["AppsSortField"]
    CREATED_AT_DESC: ClassVar["AppsSortField"]
    UPDATED_AT_DESC: ClassVar["AppsSortField"]
    USER_NAME_DESC: ClassVar["AppsSortField"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AppsSortField.NAME = AppsSortField("name")
AppsSortField.CREATED_AT = AppsSortField("created_at")
AppsSortField.UPDATED_AT = AppsSortField("updated_at")
AppsSortField.USER_NAME = AppsSortField("user_name")
AppsSortField.NAME_DESC = AppsSortField("-name")
AppsSortField.CREATED_AT_DESC = AppsSortField("-created_at")
AppsSortField.UPDATED_AT_DESC = AppsSortField("-updated_at")
AppsSortField.USER_NAME_DESC = AppsSortField("-user_name")
