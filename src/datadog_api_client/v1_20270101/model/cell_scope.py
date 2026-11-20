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
    from datadog_api_client.v1_20270101.model.cell_scope20270101_cohort_target import CellScope20270101CohortTarget
    from datadog_api_client.v1_20270101.model.cell_scope_return_period_target import CellScopeReturnPeriodTarget
    from datadog_api_client.v1_20270101.model.cell_scope_type import CellScopeType
    from datadog_api_client.v1_20270101.model.cell_scope20270101_cohort_target_one_of import (
        CellScope20270101CohortTargetOneOf,
    )
    from datadog_api_client.v1_20270101.model.cell_scope20270101_cohort_target_one_of4454617856 import (
        CellScope20270101CohortTargetOneOf4454617856,
    )


class CellScope(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.cell_scope20270101_cohort_target import CellScope20270101CohortTarget
        from datadog_api_client.v1_20270101.model.cell_scope_return_period_target import CellScopeReturnPeriodTarget
        from datadog_api_client.v1_20270101.model.cell_scope_type import CellScopeType

        return {
            "cohort_target": (CellScope20270101CohortTarget,),
            "return_period_target": (CellScopeReturnPeriodTarget,),
            "type": (CellScopeType,),
        }

    attribute_map = {
        "cohort_target": "cohort_target",
        "return_period_target": "return_period_target",
        "type": "type",
    }

    def __init__(
        self_,
        cohort_target: Union[
            CellScope20270101CohortTarget,
            CellScope20270101CohortTargetOneOf,
            CellScope20270101CohortTargetOneOf4454617856,
        ],
        return_period_target: CellScopeReturnPeriodTarget,
        type: CellScopeType,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param cohort_target: Test-only generated schema for the dashboard versioning proof of concept.
        :type cohort_target: CellScope20270101CohortTarget

        :param return_period_target: Test-only generated schema for the dashboard versioning proof of concept.
        :type return_period_target: CellScopeReturnPeriodTarget

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: CellScopeType
        """
        super().__init__(kwargs)

        self_.cohort_target = cohort_target
        self_.return_period_target = return_period_target
        self_.type = type
