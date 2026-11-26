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
    from datadog_api_client.v1_20270101.model.retention_search_return_criteria_time_interval_type import (
        RetentionSearchReturnCriteriaTimeIntervalType,
    )
    from datadog_api_client.v1_20270101.model.retention_search_return_criteria_time_interval_unit import (
        RetentionSearchReturnCriteriaTimeIntervalUnit,
    )


class RetentionSearchReturnCriteriaTimeInterval(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.retention_search_return_criteria_time_interval_type import (
            RetentionSearchReturnCriteriaTimeIntervalType,
        )
        from datadog_api_client.v1_20270101.model.retention_search_return_criteria_time_interval_unit import (
            RetentionSearchReturnCriteriaTimeIntervalUnit,
        )

        return {
            "type": (RetentionSearchReturnCriteriaTimeIntervalType,),
            "unit": (RetentionSearchReturnCriteriaTimeIntervalUnit,),
            "value": (float,),
        }

    attribute_map = {
        "type": "type",
        "unit": "unit",
        "value": "value",
    }

    def __init__(
        self_,
        type: RetentionSearchReturnCriteriaTimeIntervalType,
        unit: RetentionSearchReturnCriteriaTimeIntervalUnit,
        value: float,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: RetentionSearchReturnCriteriaTimeIntervalType

        :param unit: Test-only generated schema for the dashboard versioning proof of concept.
        :type unit: RetentionSearchReturnCriteriaTimeIntervalUnit

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: float
        """
        super().__init__(kwargs)

        self_.type = type
        self_.unit = unit
        self_.value = value
