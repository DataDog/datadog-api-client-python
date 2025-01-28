# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.patch_inbox_rules_parameters_data import PatchInboxRulesParametersData


class PatchInboxRulesParameters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_inbox_rules_parameters_data import PatchInboxRulesParametersData

        return {
            "data": (PatchInboxRulesParametersData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[PatchInboxRulesParametersData, UnsetType] = unset, **kwargs):
        """
        Body of the inbox rule patch request

        :param data: Data of the inbox rule patch request: the rule UUID, the rule type, and the rule attributes. All fields are required.
        :type data: PatchInboxRulesParametersData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
