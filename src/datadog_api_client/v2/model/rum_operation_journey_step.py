# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_operation_journey_composite_rule import RUMOperationJourneyCompositeRule
    from datadog_api_client.v2.model.rum_operation_journey_node import RUMOperationJourneyNode
    from datadog_api_client.v2.model.rum_operation_journey_step_type import RUMOperationJourneyStepType


class RUMOperationJourneyStep(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_journey_composite_rule import RUMOperationJourneyCompositeRule
        from datadog_api_client.v2.model.rum_operation_journey_node import RUMOperationJourneyNode
        from datadog_api_client.v2.model.rum_operation_journey_step_type import RUMOperationJourneyStepType

        return {
            "composite": (RUMOperationJourneyCompositeRule,),
            "nodes": ([RUMOperationJourneyNode],),
            "type": (RUMOperationJourneyStepType,),
        }

    attribute_map = {
        "composite": "composite",
        "nodes": "nodes",
        "type": "type",
    }

    def __init__(
        self_,
        type: RUMOperationJourneyStepType,
        composite: Union[RUMOperationJourneyCompositeRule, UnsetType] = unset,
        nodes: Union[List[RUMOperationJourneyNode], UnsetType] = unset,
        **kwargs,
    ):
        """
        A single step of a RUM operation's journey. Matches RUM events either through a list of ``nodes``
        or through a ``composite`` rule; the two are mutually exclusive.

        :param composite: A composite rule combining several predicates. Used as an alternative to ``nodes`` on a journey
            step when several conditions must be matched together, in any order or in a specific order.
        :type composite: RUMOperationJourneyCompositeRule, optional

        :param nodes: The list of nodes that can match this step. Mutually exclusive with ``composite``.
        :type nodes: [RUMOperationJourneyNode], optional

        :param type: The type of a step within a RUM operation's journey.
        :type type: RUMOperationJourneyStepType
        """
        if composite is not unset:
            kwargs["composite"] = composite
        if nodes is not unset:
            kwargs["nodes"] = nodes
        super().__init__(kwargs)

        self_.type = type
