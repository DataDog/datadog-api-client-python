# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SignalArchiveReason(ModelSimple):
    """
    Reason why a signal has been archived.

    :param value: Must be one of ["none", "false_positive", "testing_or_maintenance", "other"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "NONE": "none",
            "FALSE_POSITIVE": "false_positive",
            "TESTING_OR_MAINTENANCE": "testing_or_maintenance",
            "OTHER": "other",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
