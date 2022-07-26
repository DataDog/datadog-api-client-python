# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SLOTimeframe(ModelSimple):
    """
    The SLO time window options.

    :param value: Must be one of ["7d", "30d", "90d", "custom"].
    :type value: str
    """

    allowed_values = {
        "value": {
            "SEVEN_DAYS": "7d",
            "THIRTY_DAYS": "30d",
            "NINETY_DAYS": "90d",
            "CUSTOM": "custom",
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
