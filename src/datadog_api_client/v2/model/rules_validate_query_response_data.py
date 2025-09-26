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
    from datadog_api_client.v2.model.rules_validate_query_response_data_attributes import (
        RulesValidateQueryResponseDataAttributes,
    )
    from datadog_api_client.v2.model.rules_validate_query_response_data_type import RulesValidateQueryResponseDataType


class RulesValidateQueryResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rules_validate_query_response_data_attributes import (
            RulesValidateQueryResponseDataAttributes,
        )
        from datadog_api_client.v2.model.rules_validate_query_response_data_type import (
            RulesValidateQueryResponseDataType,
        )

        return {
            "attributes": (RulesValidateQueryResponseDataAttributes,),
            "id": (str,),
            "type": (RulesValidateQueryResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: RulesValidateQueryResponseDataType,
        attributes: Union[RulesValidateQueryResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``RulesValidateQueryResponseData`` object.

        :param attributes: The definition of ``RulesValidateQueryResponseDataAttributes`` object.
        :type attributes: RulesValidateQueryResponseDataAttributes, optional

        :param id: The ``RulesValidateQueryResponseData`` ``id``.
        :type id: str, optional

        :param type: Validate response resource type.
        :type type: RulesValidateQueryResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
