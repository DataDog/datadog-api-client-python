# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class ListStreamSource(ModelSimple):

    allowed_values = {
        "value": {
            "LOGS_STREAM": "logs_stream",
            "AUDIT_STREAM": "audit_stream",
            "RUM_ISSUE_STREAM": "rum_issue_stream",
            "APM_ISSUE_STREAM": "apm_issue_stream",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }

    def __init__(self, *args, **kwargs):
        """
        Source from which to query items to display in the stream.

        Note that value can be passed either in args or in kwargs, but not in both.

        :param value: If omitted defaults to "apm_issue_stream". Must be one of ["logs_stream", "audit_stream", "rum_issue_stream", "apm_issue_stream"].
        :type value: str
        """
        super().__init__(kwargs)

        if "value" in kwargs:
            value = kwargs.pop("value")
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            value = "apm_issue_stream"

        self._check_pos_args(args)

        self.value = value

        self._check_kw_args(kwargs)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""
        return cls(*args, **kwargs)
