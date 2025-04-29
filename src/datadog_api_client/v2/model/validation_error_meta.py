# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ValidationErrorMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "field": (str,),
            "id": (str,),
            "message": (str,),
        }

    attribute_map = {
        "field": "field",
        "id": "id",
        "message": "message",
    }

    def __init__(
        self_, message: str, field: Union[str, UnsetType] = unset, id: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        Describes additional metadata for validation errors, including field names and error messages.

        :param field: The field name that caused the error.
        :type field: str, optional

        :param id: The ID of the component in which the error occurred.
        :type id: str, optional

        :param message: The detailed error message.
        :type message: str
        """
        if field is not unset:
            kwargs["field"] = field
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.message = message
