# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class CloudWorkloadSecurityAgentRuleType(ModelSimple):
    """
    The type of the resource. The value should always be `agent_rule`.

    :param value: If omitted defaults to "agent_rule". Must be one of ["agent_rule"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "AGENT_RULE": "agent_rule",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
