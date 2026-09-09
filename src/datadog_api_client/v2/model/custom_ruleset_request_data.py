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
    from datadog_api_client.v2.model.custom_ruleset_request_data_attributes import CustomRulesetRequestDataAttributes
    from datadog_api_client.v2.model.custom_ruleset_data_type import CustomRulesetDataType


class CustomRulesetRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_ruleset_request_data_attributes import (
            CustomRulesetRequestDataAttributes,
        )
        from datadog_api_client.v2.model.custom_ruleset_data_type import CustomRulesetDataType

        return {
            "attributes": (CustomRulesetRequestDataAttributes,),
            "id": (str,),
            "type": (CustomRulesetDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CustomRulesetRequestDataAttributes, id: str, type: CustomRulesetDataType, **kwargs):
        """
        Data object for a custom ruleset create or update request. The resource ``id`` is
        required and must equal both ``attributes.name`` and, on update, the ``ruleset_name``
        path parameter; a request that omits it or supplies a different value is rejected
        with a 412 response.

        :param attributes: Attributes for creating or updating a custom ruleset. ``name`` is required and must
            equal the resource ``id`` ; the server rejects a mismatch with a 412 response.
        :type attributes: CustomRulesetRequestDataAttributes

        :param id: Ruleset identifier, which is the same as the ruleset name.
        :type id: str

        :param type: Resource type
        :type type: CustomRulesetDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
