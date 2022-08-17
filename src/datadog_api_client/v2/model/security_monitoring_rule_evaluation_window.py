# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleEvaluationWindow(ModelSimple):
    """
    A time window is specified to match when at least one of the cases matches true. This is a sliding window
        and evaluates in real time.

    :param value: Must be one of [0, 60, 300, 600, 900, 1800, 3600, 7200].
    :type value: int
    """

    allowed_values = {
        "value": {
            "ZERO_MINUTES": 0,
            "ONE_MINUTE": 60,
            "FIVE_MINUTES": 300,
            "TEN_MINUTES": 600,
            "FIFTEEN_MINUTES": 900,
            "THIRTY_MINUTES": 1800,
            "ONE_HOUR": 3600,
            "TWO_HOURS": 7200,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }
