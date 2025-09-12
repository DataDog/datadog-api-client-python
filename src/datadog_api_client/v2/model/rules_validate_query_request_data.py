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
    from datadog_api_client.v2.model.rules_validate_query_request_data_attributes import (
        RulesValidateQueryRequestDataAttributes,
    )
    from datadog_api_client.v2.model.rules_validate_query_request_data_type import RulesValidateQueryRequestDataType


class RulesValidateQueryRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rules_validate_query_request_data_attributes import (
            RulesValidateQueryRequestDataAttributes,
        )
        from datadog_api_client.v2.model.rules_validate_query_request_data_type import RulesValidateQueryRequestDataType

        return {
            "attributes": (RulesValidateQueryRequestDataAttributes,),
            "id": (str,),
            "type": (RulesValidateQueryRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: RulesValidateQueryRequestDataType,
        attributes: Union[RulesValidateQueryRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``RulesValidateQueryRequestData`` object.

        :param attributes: The definition of ``RulesValidateQueryRequestDataAttributes`` object.
        :type attributes: RulesValidateQueryRequestDataAttributes, optional

        :param id: The ``RulesValidateQueryRequestData`` ``id``.
        :type id: str, optional

        :param type: Validate query resource type.
        :type type: RulesValidateQueryRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
