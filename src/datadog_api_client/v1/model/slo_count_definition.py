# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SLOCountDefinition(ModelComposed):
    def __init__(self, **kwargs):
        """
        A count-based (metric) SLI specification, composed of three parts: the good events formula,
        the bad or total events formula, and the underlying queries.
        Exactly one of ``total_events_formula`` or ``bad_events_formula`` must be provided.

        :param good_events_formula: A formula that specifies how to combine the results of multiple queries.
        :type good_events_formula: SLOFormula

        :param queries:
        :type queries: [SLODataSourceQueryDefinition]

        :param total_events_formula: A formula that specifies how to combine the results of multiple queries.
        :type total_events_formula: SLOFormula

        :param bad_events_formula: A formula that specifies how to combine the results of multiple queries.
        :type bad_events_formula: SLOFormula
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
        from datadog_api_client.v1.model.slo_count_definition_with_total_events_formula import (
            SLOCountDefinitionWithTotalEventsFormula,
        )
        from datadog_api_client.v1.model.slo_count_definition_with_bad_events_formula import (
            SLOCountDefinitionWithBadEventsFormula,
        )

        return {
            "oneOf": [
                SLOCountDefinitionWithTotalEventsFormula,
                SLOCountDefinitionWithBadEventsFormula,
            ],
        }
