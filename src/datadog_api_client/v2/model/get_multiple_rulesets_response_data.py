# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes import (
        GetMultipleRulesetsResponseDataAttributes,
    )
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_type import GetMultipleRulesetsResponseDataType


class GetMultipleRulesetsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes import (
            GetMultipleRulesetsResponseDataAttributes,
        )
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_type import (
            GetMultipleRulesetsResponseDataType,
        )

        return {
            "attributes": (GetMultipleRulesetsResponseDataAttributes,),
            "id": (str,),
            "type": (GetMultipleRulesetsResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GetMultipleRulesetsResponseDataAttributes,
        id: str,
        type: GetMultipleRulesetsResponseDataType,
        **kwargs,
    ):
        """
        The primary data object in the get-multiple-rulesets response, containing the response attributes and resource type.

        :param attributes: The attributes of the get-multiple-rulesets response, containing the list of requested rulesets.
        :type attributes: GetMultipleRulesetsResponseDataAttributes

        :param id: The unique identifier of the get-multiple-rulesets response resource, echoed from the request.
        :type id: str

        :param type: Get multiple rulesets response resource type.
        :type type: GetMultipleRulesetsResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
