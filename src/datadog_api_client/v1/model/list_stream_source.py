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
        "logs_stream",
        "audit_stream",
        "rum_issue_stream",
        "apm_issue_stream",
        "logs_pattern_stream",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ListStreamSource.LOGS_STREAM = ListStreamSource("logs_stream")
ListStreamSource.AUDIT_STREAM = ListStreamSource("audit_stream")
ListStreamSource.RUM_ISSUE_STREAM = ListStreamSource("rum_issue_stream")
ListStreamSource.APM_ISSUE_STREAM = ListStreamSource("apm_issue_stream")
ListStreamSource.LOGS_PATTERN_STREAM = ListStreamSource("logs_pattern_stream")
