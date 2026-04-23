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


class SyntheticsTestResultFailure(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
            "internal_code": (str,),
            "internal_message": (str,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "internal_code": "internal_code",
        "internal_message": "internal_message",
        "message": "message",
    }

    def __init__(
        self_,
        code: Union[str, UnsetType] = unset,
        internal_code: Union[str, UnsetType] = unset,
        internal_message: Union[str, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Details about the failure of a Synthetic test.

        :param code: Error code for the failure.
        :type code: str, optional

        :param internal_code: Internal error code used for debugging.
        :type internal_code: str, optional

        :param internal_message: Internal error message used for debugging.
        :type internal_message: str, optional

        :param message: Error message for the failure.
        :type message: str, optional
        """
        if code is not unset:
            kwargs["code"] = code
        if internal_code is not unset:
            kwargs["internal_code"] = internal_code
        if internal_message is not unset:
            kwargs["internal_message"] = internal_message
        if message is not unset:
            kwargs["message"] = message
        super().__init__(kwargs)
