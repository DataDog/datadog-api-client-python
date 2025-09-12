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
    from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_costs_to_allocate_items import (
        ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems,
    )
    from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy import (
        ArbitraryCostUpsertRequestDataAttributesStrategy,
    )


class ArbitraryCostUpsertRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_costs_to_allocate_items import (
            ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems,
        )
        from datadog_api_client.v2.model.arbitrary_cost_upsert_request_data_attributes_strategy import (
            ArbitraryCostUpsertRequestDataAttributesStrategy,
        )

        return {
            "costs_to_allocate": ([ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems],),
            "enabled": (bool,),
            "order_id": (int,),
            "provider": ([str],),
            "rejected": (bool,),
            "rule_name": (str,),
            "strategy": (ArbitraryCostUpsertRequestDataAttributesStrategy,),
            "type": (str,),
        }

    attribute_map = {
        "costs_to_allocate": "costs_to_allocate",
        "enabled": "enabled",
        "order_id": "order_id",
        "provider": "provider",
        "rejected": "rejected",
        "rule_name": "rule_name",
        "strategy": "strategy",
        "type": "type",
    }

    def __init__(
        self_,
        costs_to_allocate: List[ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems],
        provider: List[str],
        rule_name: str,
        strategy: ArbitraryCostUpsertRequestDataAttributesStrategy,
        type: str,
        enabled: Union[bool, UnsetType] = unset,
        order_id: Union[int, UnsetType] = unset,
        rejected: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryCostUpsertRequestDataAttributes`` object.

        :param costs_to_allocate: The ``attributes`` ``costs_to_allocate``.
        :type costs_to_allocate: [ArbitraryCostUpsertRequestDataAttributesCostsToAllocateItems]

        :param enabled: The ``attributes`` ``enabled``.
        :type enabled: bool, optional

        :param order_id: The ``attributes`` ``order_id``.
        :type order_id: int, optional

        :param provider: The ``attributes`` ``provider``.
        :type provider: [str]

        :param rejected: The ``attributes`` ``rejected``.
        :type rejected: bool, optional

        :param rule_name: The ``attributes`` ``rule_name``.
        :type rule_name: str

        :param strategy: The definition of ``ArbitraryCostUpsertRequestDataAttributesStrategy`` object.
        :type strategy: ArbitraryCostUpsertRequestDataAttributesStrategy

        :param type: The ``attributes`` ``type``.
        :type type: str
        """
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if order_id is not unset:
            kwargs["order_id"] = order_id
        if rejected is not unset:
            kwargs["rejected"] = rejected
        super().__init__(kwargs)

        self_.costs_to_allocate = costs_to_allocate
        self_.provider = provider
        self_.rule_name = rule_name
        self_.strategy = strategy
        self_.type = type
