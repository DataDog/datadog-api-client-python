# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CsmUnifiedHostSource(ModelSimple):
    """
    The source of a unified host entry, indicating whether it was discovered via agent, agentless scanning, or both.

    :param value: Must be one of ["agent", "agentless", "both"].
    :type value: str
    """

    allowed_values = {
        "agent",
        "agentless",
        "both",
    }
    AGENT: ClassVar["CsmUnifiedHostSource"]
    AGENTLESS: ClassVar["CsmUnifiedHostSource"]
    BOTH: ClassVar["CsmUnifiedHostSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CsmUnifiedHostSource.AGENT = CsmUnifiedHostSource("agent")
CsmUnifiedHostSource.AGENTLESS = CsmUnifiedHostSource("agentless")
CsmUnifiedHostSource.BOTH = CsmUnifiedHostSource("both")
