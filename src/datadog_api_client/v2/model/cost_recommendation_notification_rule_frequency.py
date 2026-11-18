# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CostRecommendationNotificationRuleFrequency(ModelSimple):
    """
    How often the digest is sent. `weekly` and `biweekly` use `weekly_execution_day` and `weekly_execution_time`;
        `every_30` and `every_90` (days) use `interval_execution_date` and `interval_execution_time`.

    :param value: Must be one of ["weekly", "biweekly", "every_30", "every_90"].
    :type value: str
    """

    allowed_values = {
        "weekly",
        "biweekly",
        "every_30",
        "every_90",
    }
    WEEKLY: ClassVar["CostRecommendationNotificationRuleFrequency"]
    BIWEEKLY: ClassVar["CostRecommendationNotificationRuleFrequency"]
    EVERY_30: ClassVar["CostRecommendationNotificationRuleFrequency"]
    EVERY_90: ClassVar["CostRecommendationNotificationRuleFrequency"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CostRecommendationNotificationRuleFrequency.WEEKLY = CostRecommendationNotificationRuleFrequency("weekly")
CostRecommendationNotificationRuleFrequency.BIWEEKLY = CostRecommendationNotificationRuleFrequency("biweekly")
CostRecommendationNotificationRuleFrequency.EVERY_30 = CostRecommendationNotificationRuleFrequency("every_30")
CostRecommendationNotificationRuleFrequency.EVERY_90 = CostRecommendationNotificationRuleFrequency("every_90")
