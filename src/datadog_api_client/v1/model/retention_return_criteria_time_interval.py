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
    from datadog_api_client.v1.model.retention_return_criteria_time_interval_type import (
        RetentionReturnCriteriaTimeIntervalType,
    )
    from datadog_api_client.v1.model.retention_return_criteria_time_interval_unit import (
        RetentionReturnCriteriaTimeIntervalUnit,
    )


class RetentionReturnCriteriaTimeInterval(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.retention_return_criteria_time_interval_type import (
            RetentionReturnCriteriaTimeIntervalType,
        )
        from datadog_api_client.v1.model.retention_return_criteria_time_interval_unit import (
            RetentionReturnCriteriaTimeIntervalUnit,
        )

        return {
            "type": (RetentionReturnCriteriaTimeIntervalType,),
            "unit": (RetentionReturnCriteriaTimeIntervalUnit,),
            "value": (float,),
        }

    attribute_map = {
        "type": "type",
        "unit": "unit",
        "value": "value",
    }

    def __init__(
        self_,
        type: RetentionReturnCriteriaTimeIntervalType,
        unit: RetentionReturnCriteriaTimeIntervalUnit,
        value: float,
        **kwargs,
    ):
        """
        Time interval for return criteria.

        :param type: Type of time interval for return criteria.
        :type type: RetentionReturnCriteriaTimeIntervalType

        :param unit: Unit of time for retention return criteria interval.
        :type unit: RetentionReturnCriteriaTimeIntervalUnit

        :param value: Value of the time interval.
        :type value: float
        """
        super().__init__(kwargs)

        self_.type = type
        self_.unit = unit
        self_.value = value
