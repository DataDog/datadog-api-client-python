# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class LogsGrokParserType(ModelSimple):
    """
    Type of logs grok parser.

    :param value: If omitted defaults to "grok-parser". Must be one of ["grok-parser"].
    :type value: str
    """

    allowed_values = {
        "grok-parser",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


LogsGrokParserType.GROK_PARSER = LogsGrokParserType("grok-parser")
