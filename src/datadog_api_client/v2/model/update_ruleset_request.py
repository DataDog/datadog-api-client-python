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
    from datadog_api_client.v2.model.update_ruleset_request_data import UpdateRulesetRequestData


class UpdateRulesetRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_ruleset_request_data import UpdateRulesetRequestData

        return {
            "data": (UpdateRulesetRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[UpdateRulesetRequestData, UnsetType] = unset, **kwargs):
        """
        The definition of ``UpdateRulesetRequest`` object.

        :param data: The definition of ``UpdateRulesetRequestData`` object.
        :type data: UpdateRulesetRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
