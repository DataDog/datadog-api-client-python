# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class ServiceCheckStatus(ModelSimple):
    """
    The status of a service check.

    :param value: Must be one of [0, 1, 2, 3].
    :type value: int
    """

    allowed_values = {
        "value": {
            "OK": 0,
            "WARNING": 1,
            "CRITICAL": 2,
            "UNKNOWN": 3,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }
