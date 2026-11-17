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


class SecurityMonitoringBatchMigrationPublishErrorDetail(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "code": (str,),
            "message": (str,),
            "target": (str,),
        }

    attribute_map = {
        "code": "code",
        "message": "message",
        "target": "target",
    }

    def __init__(
        self_,
        code: Union[str, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        target: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A rule validation error.

        :param code: The error code.
        :type code: str, optional

        :param message: The error message.
        :type message: str, optional

        :param target: The rule field the error applies to.
        :type target: str, optional
        """
        if code is not unset:
            kwargs["code"] = code
        if message is not unset:
            kwargs["message"] = message
        if target is not unset:
            kwargs["target"] = target
        super().__init__(kwargs)
