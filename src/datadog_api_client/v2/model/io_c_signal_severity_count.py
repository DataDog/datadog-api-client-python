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


class IoCSignalSeverityCount(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "count": (int,),
            "severity": (str,),
        }

    attribute_map = {
        "count": "count",
        "severity": "severity",
    }

    def __init__(self_, count: Union[int, UnsetType] = unset, severity: Union[str, UnsetType] = unset, **kwargs):
        """
        Count of security signals by severity level.

        :param count: Number of signals at this severity level.
        :type count: int, optional

        :param severity: Severity level (for example, critical, high, medium, low, info).
        :type severity: str, optional
        """
        if count is not unset:
            kwargs["count"] = count
        if severity is not unset:
            kwargs["severity"] = severity
        super().__init__(kwargs)
