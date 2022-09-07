# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class AuditLogsResponseStatus(ModelSimple):
    """
    The status of the response.

    :param value: Must be one of ["done", "timeout"].
    :type value: str
    """

    allowed_values = {
        "done",
        "timeout",
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AuditLogsResponseStatus.DONE = AuditLogsResponseStatus("done")
AuditLogsResponseStatus.TIMEOUT = AuditLogsResponseStatus("timeout")
