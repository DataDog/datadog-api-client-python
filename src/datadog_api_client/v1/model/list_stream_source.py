# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class ListStreamSource(ModelSimple):
    """
    Source from which to query items to display in the stream.

    :param value: If omitted defaults to "apm_issue_stream". Must be one of ["logs_stream", "audit_stream", "rum_issue_stream", "apm_issue_stream", "logs_pattern_stream"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "LOGS_STREAM": "logs_stream",
            "AUDIT_STREAM": "audit_stream",
            "RUM_ISSUE_STREAM": "rum_issue_stream",
            "APM_ISSUE_STREAM": "apm_issue_stream",
            "LOGS_PATTERN_STREAM": "logs_pattern_stream",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
