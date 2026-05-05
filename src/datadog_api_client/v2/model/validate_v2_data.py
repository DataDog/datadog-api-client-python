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
    from datadog_api_client.v2.model.validate_v2_attributes import ValidateV2Attributes
    from datadog_api_client.v2.model.validate_v2_type import ValidateV2Type


class ValidateV2Data(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.validate_v2_attributes import ValidateV2Attributes
        from datadog_api_client.v2.model.validate_v2_type import ValidateV2Type

        return {
            "attributes": (ValidateV2Attributes,),
            "id": (str,),
            "type": (ValidateV2Type,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: ValidateV2Attributes, id: str, type: ValidateV2Type, **kwargs):
        """
        Data object containing the API key validation result.

        :param attributes: Attributes of the API key validation response.
        :type attributes: ValidateV2Attributes

        :param id: The UUID of the organization associated with the API key.
        :type id: str

        :param type: Resource type for the API key validation response.
        :type type: ValidateV2Type
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
