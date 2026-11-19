# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ExperimentsStopBanditV2RequestDataType(ModelSimple):
    """
    Stop bandit request resource type.

    :param value: If omitted defaults to "stop-bandit-request". Must be one of ["stop-bandit-request"].
    :type value: str
    """

    allowed_values = {
        "stop-bandit-request",
    }
    STOP_BANDIT_REQUEST: ClassVar["ExperimentsStopBanditV2RequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ExperimentsStopBanditV2RequestDataType.STOP_BANDIT_REQUEST = ExperimentsStopBanditV2RequestDataType(
    "stop-bandit-request"
)
