# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class LogsArchiveState(ModelSimple):
    """
    The state of the archive.

    :param value: Must be one of ["UNKNOWN", "WORKING", "FAILING", "WORKING_AUTH_LEGACY"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "UNKNOWN": "UNKNOWN",
            "WORKING": "WORKING",
            "FAILING": "FAILING",
            "WORKING_AUTH_LEGACY": "WORKING_AUTH_LEGACY",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
