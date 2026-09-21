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


class SnowflakeSecurityLogsIntegrationDataflowSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "security_logs_interval_min": (int,),
        }

    attribute_map = {
        "security_logs_interval_min": "security_logs_interval_min",
    }

    def __init__(self_, security_logs_interval_min: Union[int, UnsetType] = unset, **kwargs):
        """
        Settings of the security logs dataflow.

        :param security_logs_interval_min: How often security logs are collected, in minutes.
        :type security_logs_interval_min: int, optional
        """
        if security_logs_interval_min is not unset:
            kwargs["security_logs_interval_min"] = security_logs_interval_min
        super().__init__(kwargs)
