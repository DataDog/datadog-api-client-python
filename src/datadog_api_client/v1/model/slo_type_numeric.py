# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SLOTypeNumeric(ModelSimple):
    """
    A numeric representation of the type of the service level objective (`0` for
        monitor, `1` for metric). Always included in service level objective responses.
        Ignored in create/update requests.

    :param value: Must be one of [0, 1].
    :type value: int
    """

    allowed_values = {
        "value": {
            "MONITOR": 0,
            "METRIC": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }
