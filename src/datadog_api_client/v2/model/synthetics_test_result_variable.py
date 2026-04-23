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


class SyntheticsTestResultVariable(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "err": (str,),
            "error_message": (str,),
            "example": (str,),
            "id": (str,),
            "name": (str,),
            "pattern": (str,),
            "secure": (bool,),
            "type": (str,),
            "val": (str,),
            "value": (str,),
        }

    attribute_map = {
        "err": "err",
        "error_message": "error_message",
        "example": "example",
        "id": "id",
        "name": "name",
        "pattern": "pattern",
        "secure": "secure",
        "type": "type",
        "val": "val",
        "value": "value",
    }

    def __init__(
        self_,
        err: Union[str, UnsetType] = unset,
        error_message: Union[str, UnsetType] = unset,
        example: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        pattern: Union[str, UnsetType] = unset,
        secure: Union[bool, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        val: Union[str, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A variable used or extracted during a test.

        :param err: Error encountered when evaluating the variable.
        :type err: str, optional

        :param error_message: Human-readable error message for variable evaluation.
        :type error_message: str, optional

        :param example: Example value for the variable.
        :type example: str, optional

        :param id: Variable identifier.
        :type id: str, optional

        :param name: Variable name.
        :type name: str, optional

        :param pattern: Pattern used to extract the variable.
        :type pattern: str, optional

        :param secure: Whether the variable holds a secure value.
        :type secure: bool, optional

        :param type: Variable type.
        :type type: str, optional

        :param val: Evaluated value of the variable.
        :type val: str, optional

        :param value: Current value of the variable.
        :type value: str, optional
        """
        if err is not unset:
            kwargs["err"] = err
        if error_message is not unset:
            kwargs["error_message"] = error_message
        if example is not unset:
            kwargs["example"] = example
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if pattern is not unset:
            kwargs["pattern"] = pattern
        if secure is not unset:
            kwargs["secure"] = secure
        if type is not unset:
            kwargs["type"] = type
        if val is not unset:
            kwargs["val"] = val
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
