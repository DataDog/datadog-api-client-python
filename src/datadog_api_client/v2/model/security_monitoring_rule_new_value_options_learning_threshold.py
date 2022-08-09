# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleNewValueOptionsLearningThreshold(ModelSimple):
    """
    A number of occurrences after which signals will be generated for values that weren't learned.

    :param value: If omitted defaults to 0. Must be one of [0, 1].
    :type value: int
    """

    allowed_values = {
        "value": {
            "ZERO_OCCURRENCES": 0,
            "ONE_OCCURRENCE": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }
