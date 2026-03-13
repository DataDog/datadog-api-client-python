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
    from datadog_api_client.v1.model.slo_count_definition import SLOCountDefinition
    from datadog_api_client.v1.model.slo_count_definition_with_total_events_formula import (
        SLOCountDefinitionWithTotalEventsFormula,
    )
    from datadog_api_client.v1.model.slo_count_definition_with_bad_events_formula import (
        SLOCountDefinitionWithBadEventsFormula,
    )


class SLOCountSpec(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_count_definition import SLOCountDefinition

        return {
            "count": (SLOCountDefinition,),
        }

    attribute_map = {
        "count": "count",
    }

    def __init__(
        self_,
        count: Union[
            SLOCountDefinition, SLOCountDefinitionWithTotalEventsFormula, SLOCountDefinitionWithBadEventsFormula
        ],
        **kwargs,
    ):
        """
        A metric SLI specification.

        :param count: A count-based (metric) SLI specification, composed of three parts: the good events formula,
            the bad or total events formula, and the underlying queries.
            Exactly one of ``total_events_formula`` or ``bad_events_formula`` must be provided.
        :type count: SLOCountDefinition
        """
        super().__init__(kwargs)

        self_.count = count
