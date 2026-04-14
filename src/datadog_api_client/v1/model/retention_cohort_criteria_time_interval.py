# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.retention_cohort_criteria_time_interval_type import (
        RetentionCohortCriteriaTimeIntervalType,
    )
    from datadog_api_client.v1.model.calendar_interval import CalendarInterval


class RetentionCohortCriteriaTimeInterval(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.retention_cohort_criteria_time_interval_type import (
            RetentionCohortCriteriaTimeIntervalType,
        )
        from datadog_api_client.v1.model.calendar_interval import CalendarInterval

        return {
            "type": (RetentionCohortCriteriaTimeIntervalType,),
            "value": (CalendarInterval,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self_, type: RetentionCohortCriteriaTimeIntervalType, value: CalendarInterval, **kwargs):
        """
        Time interval for cohort criteria.

        :param type: Type of time interval for cohort criteria.
        :type type: RetentionCohortCriteriaTimeIntervalType

        :param value: Calendar interval definition.
        :type value: CalendarInterval
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
