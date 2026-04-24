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


class SyntheticsFastTestResultFailure(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
            "message": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
    }

    def __init__(self_, code: Union[str, UnsetType] = unset, message: Union[str, UnsetType] = unset, **kwargs):
        """
        Failure details if the fast test did not pass.

        :param code: Error code identifying the failure type.
        :type code: str, optional

        :param message: Human-readable description of the failure.
        :type message: str, optional
        """
        if code is not unset:
            kwargs["code"] = code
        if message is not unset:
            kwargs["message"] = message
        super().__init__(kwargs)
