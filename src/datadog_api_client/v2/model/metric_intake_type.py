# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class MetricIntakeType(ModelSimple):
    """
    The type of metric. The available types are `0` (unspecified), `1` (count), `2` (rate), and `3` (gauge).

    :param value: Must be one of [0, 1, 2, 3].
    :type value: int
    """

    allowed_values = {
        "value": {
            "UNSPECIFIED": 0,
            "COUNT": 1,
            "RATE": 2,
            "GAUGE": 3,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }
