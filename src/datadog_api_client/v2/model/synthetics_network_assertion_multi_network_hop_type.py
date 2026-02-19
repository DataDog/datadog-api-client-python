# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SyntheticsNetworkAssertionMultiNetworkHopType(ModelSimple):
    """
    Type of the multi-network hop assertion.

    :param value: If omitted defaults to "multiNetworkHop". Must be one of ["multiNetworkHop"].
    :type value: str
    """

    allowed_values = {
        "multiNetworkHop",
    }
    MULTI_NETWORK_HOP: ClassVar["SyntheticsNetworkAssertionMultiNetworkHopType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SyntheticsNetworkAssertionMultiNetworkHopType.MULTI_NETWORK_HOP = SyntheticsNetworkAssertionMultiNetworkHopType(
    "multiNetworkHop"
)
