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
    from datadog_api_client.v2.model.reorder_mute_rules_parameters_data import ReorderMuteRulesParametersData


class ReorderMuteRulesParameters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.reorder_mute_rules_parameters_data import ReorderMuteRulesParametersData

        return {
            "data": ([ReorderMuteRulesParametersData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[ReorderMuteRulesParametersData], UnsetType] = unset, **kwargs):
        """
        Body of the mute rule reorder request: the full list of mute rules, which must be provided in the new order.

        :param data: The ``ReorderMuteRulesParameters`` ``data``.
        :type data: [ReorderMuteRulesParametersData], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
