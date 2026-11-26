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
    from datadog_api_client.v1_20270101.model.cell_scope_cohort_target_aggregation_type import (
        CellScopeCohortTargetAggregationType,
    )
    from datadog_api_client.v1_20270101.model.cell_scope_cohort_target_any_of_any_of_item_value import (
        CellScopeCohortTargetAnyOfAnyOfItemValue,
    )


class CellScope20270101CohortTargetOneOf4454617856(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.cell_scope_cohort_target_aggregation_type import (
            CellScopeCohortTargetAggregationType,
        )
        from datadog_api_client.v1_20270101.model.cell_scope_cohort_target_any_of_any_of_item_value import (
            CellScopeCohortTargetAnyOfAnyOfItemValue,
        )

        return {
            "type": (CellScopeCohortTargetAggregationType,),
            "value": (CellScopeCohortTargetAnyOfAnyOfItemValue,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_, type: CellScopeCohortTargetAggregationType, value: CellScopeCohortTargetAnyOfAnyOfItemValue, **kwargs
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: CellScopeCohortTargetAggregationType

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: CellScopeCohortTargetAnyOfAnyOfItemValue
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
