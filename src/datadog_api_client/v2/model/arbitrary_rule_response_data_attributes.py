# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_costs_to_allocate_items import (
        ArbitraryRuleResponseDataAttributesCostsToAllocateItems,
    )
    from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy import (
        ArbitraryRuleResponseDataAttributesStrategy,
    )


class ArbitraryRuleResponseDataAttributes(ModelNormal):
    validations = {
        "version": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_costs_to_allocate_items import (
            ArbitraryRuleResponseDataAttributesCostsToAllocateItems,
        )
        from datadog_api_client.v2.model.arbitrary_rule_response_data_attributes_strategy import (
            ArbitraryRuleResponseDataAttributesStrategy,
        )

        return {
            "costs_to_allocate": ([ArbitraryRuleResponseDataAttributesCostsToAllocateItems],),
            "created": (datetime,),
            "enabled": (bool,),
            "last_modified_user_uuid": (str,),
            "order_id": (int,),
            "processing_status": (str,),
            "provider": ([str],),
            "rejected": (bool,),
            "rule_name": (str,),
            "strategy": (ArbitraryRuleResponseDataAttributesStrategy,),
            "type": (str,),
            "updated": (datetime,),
            "version": (int,),
        }

    attribute_map = {
        "costs_to_allocate": "costs_to_allocate",
        "created": "created",
        "enabled": "enabled",
        "last_modified_user_uuid": "last_modified_user_uuid",
        "order_id": "order_id",
        "processing_status": "processing_status",
        "provider": "provider",
        "rejected": "rejected",
        "rule_name": "rule_name",
        "strategy": "strategy",
        "type": "type",
        "updated": "updated",
        "version": "version",
    }

    def __init__(
        self_,
        costs_to_allocate: List[ArbitraryRuleResponseDataAttributesCostsToAllocateItems],
        created: datetime,
        enabled: bool,
        last_modified_user_uuid: str,
        order_id: int,
        provider: List[str],
        rule_name: str,
        strategy: ArbitraryRuleResponseDataAttributesStrategy,
        type: str,
        updated: datetime,
        version: int,
        processing_status: Union[str, UnsetType] = unset,
        rejected: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ArbitraryRuleResponseDataAttributes`` object.

        :param costs_to_allocate: The ``attributes`` ``costs_to_allocate``.
        :type costs_to_allocate: [ArbitraryRuleResponseDataAttributesCostsToAllocateItems]

        :param created: The ``attributes`` ``created``.
        :type created: datetime

        :param enabled: The ``attributes`` ``enabled``.
        :type enabled: bool

        :param last_modified_user_uuid: The ``attributes`` ``last_modified_user_uuid``.
        :type last_modified_user_uuid: str

        :param order_id: The ``attributes`` ``order_id``.
        :type order_id: int

        :param processing_status: The ``attributes`` ``processing_status``.
        :type processing_status: str, optional

        :param provider: The ``attributes`` ``provider``.
        :type provider: [str]

        :param rejected: The ``attributes`` ``rejected``.
        :type rejected: bool, optional

        :param rule_name: The ``attributes`` ``rule_name``.
        :type rule_name: str

        :param strategy: The definition of ``ArbitraryRuleResponseDataAttributesStrategy`` object.
        :type strategy: ArbitraryRuleResponseDataAttributesStrategy

        :param type: The ``attributes`` ``type``.
        :type type: str

        :param updated: The ``attributes`` ``updated``.
        :type updated: datetime

        :param version: The ``attributes`` ``version``.
        :type version: int
        """
        if processing_status is not unset:
            kwargs["processing_status"] = processing_status
        if rejected is not unset:
            kwargs["rejected"] = rejected
        super().__init__(kwargs)

        self_.costs_to_allocate = costs_to_allocate
        self_.created = created
        self_.enabled = enabled
        self_.last_modified_user_uuid = last_modified_user_uuid
        self_.order_id = order_id
        self_.provider = provider
        self_.rule_name = rule_name
        self_.strategy = strategy
        self_.type = type
        self_.updated = updated
        self_.version = version
