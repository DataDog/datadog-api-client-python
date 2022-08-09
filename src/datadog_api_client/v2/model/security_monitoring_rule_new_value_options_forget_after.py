# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)


class SecurityMonitoringRuleNewValueOptionsForgetAfter(ModelSimple):
    """
    The duration in days after which a learned value is forgotten.

    :param value: Must be one of [1, 2, 7, 14, 21, 28].
    :type value: int
    """

    allowed_values = {
        "value": {
            "ONE_DAY": 1,
            "TWO_DAYS": 2,
            "ONE_WEEK": 7,
            "TWO_WEEKS": 14,
            "THREE_WEEKS": 21,
            "FOUR_WEEKS": 28,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }
