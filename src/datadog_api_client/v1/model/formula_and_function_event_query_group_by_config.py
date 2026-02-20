# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class FormulaAndFunctionEventQueryGroupByConfig(ModelComposed):
    def __init__(self, **kwargs):
        """
        Group by configuration for a formula and functions events query. Can be a list of facet objects or a flat object with a list of fields.

        :param fields: List of event facets to group by.
        :type fields: [str]

        :param limit: Number of groups to return.
        :type limit: int, optional

        :param sort: Options for sorting group by results.
        :type sort: FormulaAndFunctionEventQueryGroupBySort, optional
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
        from datadog_api_client.v1.model.formula_and_function_event_query_group_by import (
            FormulaAndFunctionEventQueryGroupBy,
        )
        from datadog_api_client.v1.model.formula_and_function_event_query_group_by_fields import (
            FormulaAndFunctionEventQueryGroupByFields,
        )

        return {
            "oneOf": [
                [FormulaAndFunctionEventQueryGroupBy],
                FormulaAndFunctionEventQueryGroupByFields,
            ],
        }
