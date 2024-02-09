# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.security_monitoring_suppression import SecurityMonitoringSuppression


class SecurityMonitoringSuppressionResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.security_monitoring_suppression import SecurityMonitoringSuppression

        return {
            "data": (SecurityMonitoringSuppression,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[SecurityMonitoringSuppression, UnsetType] = unset, **kwargs):
        """
        Response object containing a single suppression rule.

        :param data: The suppression rule's properties.
        :type data: SecurityMonitoringSuppression, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
