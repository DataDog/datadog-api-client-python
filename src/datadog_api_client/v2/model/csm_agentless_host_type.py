# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CsmAgentlessHostType(ModelSimple):
    """
    The JSON:API type for agentless host resources. The value should always be `agentless_host`.

    :param value: If omitted defaults to "agentless_host". Must be one of ["agentless_host"].
    :type value: str
    """

    allowed_values = {
        "agentless_host",
    }
    AGENTLESS_HOST: ClassVar["CsmAgentlessHostType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CsmAgentlessHostType.AGENTLESS_HOST = CsmAgentlessHostType("agentless_host")
