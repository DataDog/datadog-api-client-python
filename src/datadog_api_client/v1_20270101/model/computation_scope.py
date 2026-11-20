# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class ComputationScope(ModelComposed):
    def __init__(self, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param target: Test-only generated schema for the dashboard versioning proof of concept.
        :type target: CohortScope20270101Target

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: CohortScopeType

        :param cohort_target: Test-only generated schema for the dashboard versioning proof of concept.
        :type cohort_target: CellScope20270101CohortTarget

        :param return_period_target: Test-only generated schema for the dashboard versioning proof of concept.
        :type return_period_target: CellScopeReturnPeriodTarget
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1_20270101.model.cohort_scope import CohortScope
        from datadog_api_client.v1_20270101.model.return_period_scope import ReturnPeriodScope
        from datadog_api_client.v1_20270101.model.cell_scope import CellScope

        return {
            "oneOf": [
                CohortScope,
                ReturnPeriodScope,
                CellScope,
            ],
        }
