# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SecurityMonitoringSuppressionType(ModelSimple):
    """
    The type of the resource. The value should always be `suppressions`.

    :param value: If omitted defaults to "suppressions". Must be one of ["suppressions"].
    :type value: str
    """

    allowed_values = {
        "suppressions",
    }
    SUPPRESSIONS: ClassVar["SecurityMonitoringSuppressionType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SecurityMonitoringSuppressionType.SUPPRESSIONS = SecurityMonitoringSuppressionType("suppressions")
