# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultHealthCheck(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "message": ({str: (str,)},),
            "status": (int,),
        }

    attribute_map = {
        "message": "message",
        "status": "status",
    }

    def __init__(
        self_, message: Union[Dict[str, str], UnsetType] = unset, status: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Health check information returned from a gRPC health check call.

        :param message: Raw health check message payload.
        :type message: {str: (str,)}, optional

        :param status: Health check status code.
        :type status: int, optional
        """
        if message is not unset:
            kwargs["message"] = message
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
