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
    from datadog_api_client.v2.model.reorder_inbox_rules_parameters_data import ReorderInboxRulesParametersData


class ReorderInboxRulesParameters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.reorder_inbox_rules_parameters_data import ReorderInboxRulesParametersData

        return {
            "data": ([ReorderInboxRulesParametersData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[ReorderInboxRulesParametersData], UnsetType] = unset, **kwargs):
        """
        Body of the inbox rule reorder request: the full list of inbox rules needs to be provided in the new order.

        :param data: The ``ReorderInboxRulesParameters`` ``data``.
        :type data: [ReorderInboxRulesParametersData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
