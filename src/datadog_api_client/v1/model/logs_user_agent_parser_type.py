# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class LogsUserAgentParserType(StringEnum):
    """
    Type of logs User-Agent parser.

    :param value: If omitted defaults to "user-agent-parser". Must be one of ["user-agent-parser"].
    :type value: str
    """

    allowed_values = {
        "user-agent-parser",
    }
    USER_AGENT_PARSER: ClassVar["LogsUserAgentParserType"]


LogsUserAgentParserType.USER_AGENT_PARSER = LogsUserAgentParserType("user-agent-parser")
