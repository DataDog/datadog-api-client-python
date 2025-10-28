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
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItems,
    )


class GetMultipleRulesetsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItems,
        )

        return {
            "rulesets": ([GetMultipleRulesetsResponseDataAttributesRulesetsItems],),
        }

    attribute_map = {
        "rulesets": "rulesets",
    }

    def __init__(
        self_,
        rulesets: Union[List[GetMultipleRulesetsResponseDataAttributesRulesetsItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param rulesets:
        :type rulesets: [GetMultipleRulesetsResponseDataAttributesRulesetsItems], optional
        """
        if rulesets is not unset:
            kwargs["rulesets"] = rulesets
        super().__init__(kwargs)
