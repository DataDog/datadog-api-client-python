# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AiGatewayProviderStatusState(ModelSimple):
    """
    Whether the provider is working. `checking` means no observation has been recorded yet, not that a
        check is running.

    :param value: Must be one of ["ok", "invalid", "checking"].
    :type value: str
    """

    allowed_values = {
        "ok",
        "invalid",
        "checking",
    }
    OK: ClassVar["AiGatewayProviderStatusState"]
    INVALID: ClassVar["AiGatewayProviderStatusState"]
    CHECKING: ClassVar["AiGatewayProviderStatusState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AiGatewayProviderStatusState.OK = AiGatewayProviderStatusState("ok")
AiGatewayProviderStatusState.INVALID = AiGatewayProviderStatusState("invalid")
AiGatewayProviderStatusState.CHECKING = AiGatewayProviderStatusState("checking")
