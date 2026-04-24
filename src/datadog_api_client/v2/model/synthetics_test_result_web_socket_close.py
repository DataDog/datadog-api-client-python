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


class SyntheticsTestResultWebSocketClose(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "reason": (str,),
            "status_code": (int,),
        }

    attribute_map = {
        "reason": "reason",
        "status_code": "status_code",
    }

    def __init__(self_, reason: Union[str, UnsetType] = unset, status_code: Union[int, UnsetType] = unset, **kwargs):
        """
        WebSocket close frame information for WebSocket test responses.

        :param reason: Reason string received in the close frame.
        :type reason: str, optional

        :param status_code: Status code received in the close frame.
        :type status_code: int, optional
        """
        if reason is not unset:
            kwargs["reason"] = reason
        if status_code is not unset:
            kwargs["status_code"] = status_code
        super().__init__(kwargs)
