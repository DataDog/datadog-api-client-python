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
    from datadog_api_client.v1_20270101.model.occurrence_filter_operator import OccurrenceFilterOperator
    from datadog_api_client.v1_20270101.model.occurrence_filter_value import OccurrenceFilterValue


class OccurrenceFilter(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.occurrence_filter_operator import OccurrenceFilterOperator
        from datadog_api_client.v1_20270101.model.occurrence_filter_value import OccurrenceFilterValue

        return {
            "operator": (OccurrenceFilterOperator,),
            "value": (OccurrenceFilterValue,),
        }

    attribute_map = {
        "operator": "operator",
        "value": "value",
    }

    def __init__(self_, operator: OccurrenceFilterOperator, value: OccurrenceFilterValue, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param operator: Test-only generated schema for the dashboard versioning proof of concept.
        :type operator: OccurrenceFilterOperator

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: OccurrenceFilterValue
        """
        super().__init__(kwargs)

        self_.operator = operator
        self_.value = value
