# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringSignalState(ModelSimple):
    """
    The new triage state of the signal.

    :param value: Must be one of ["open", "archived", "under_review"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "OPEN": "open",
            "ARCHIVED": "archived",
            "UNDER_REVIEW": "under_review",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
