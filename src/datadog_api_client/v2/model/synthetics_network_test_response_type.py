# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsNetworkTestResponseType(ModelSimple):
    """
    Type of response, `network_test`.

    :param value: If omitted defaults to "network_test". Must be one of ["network_test"].
    :type value: str
    """

    allowed_values = {
        "network_test",
    }
    NETWORK_TEST: ClassVar["SyntheticsNetworkTestResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsNetworkTestResponseType.NETWORK_TEST = SyntheticsNetworkTestResponseType("network_test")
