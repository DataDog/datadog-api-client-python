# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.retention_search_cohort_criteria_time_interval_type import (
        RetentionSearchCohortCriteriaTimeIntervalType,
    )
    from datadog_api_client.v1_20270101.model.retention_search_cohort_criteria_time_interval20270101_value import (
        RetentionSearchCohortCriteriaTimeInterval20270101Value,
    )
    from datadog_api_client.v1_20270101.model.calendar_interval_day import CalendarIntervalDay
    from datadog_api_client.v1_20270101.model.calendar_interval_week import CalendarIntervalWeek
    from datadog_api_client.v1_20270101.model.calendar_interval_month import CalendarIntervalMonth


class RetentionSearchCohortCriteriaTimeInterval(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.retention_search_cohort_criteria_time_interval_type import (
            RetentionSearchCohortCriteriaTimeIntervalType,
        )
        from datadog_api_client.v1_20270101.model.retention_search_cohort_criteria_time_interval20270101_value import (
            RetentionSearchCohortCriteriaTimeInterval20270101Value,
        )

        return {
            "type": (RetentionSearchCohortCriteriaTimeIntervalType,),
            "value": (RetentionSearchCohortCriteriaTimeInterval20270101Value,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        type: RetentionSearchCohortCriteriaTimeIntervalType,
        value: Union[
            RetentionSearchCohortCriteriaTimeInterval20270101Value,
            CalendarIntervalDay,
            CalendarIntervalWeek,
            CalendarIntervalMonth,
        ],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: RetentionSearchCohortCriteriaTimeIntervalType

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: RetentionSearchCohortCriteriaTimeInterval20270101Value
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
