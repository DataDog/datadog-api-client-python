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
    from datadog_api_client.v2.model.get_ast_response_data_attributes import GetAstResponseDataAttributes
    from datadog_api_client.v2.model.get_ast_response_data_type import GetAstResponseDataType


class GetAstResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_ast_response_data_attributes import GetAstResponseDataAttributes
        from datadog_api_client.v2.model.get_ast_response_data_type import GetAstResponseDataType

        return {
            "attributes": (GetAstResponseDataAttributes,),
            "id": (str,),
            "type": (GetAstResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: GetAstResponseDataAttributes, id: str, type: GetAstResponseDataType, **kwargs):
        """
        The primary data object in the get-AST response.

        :param attributes: The attributes of the get-AST response, containing the parsed abstract syntax tree.
        :type attributes: GetAstResponseDataAttributes

        :param id: The identifier of the get-AST response resource, echoed from the request.
        :type id: str

        :param type: Get AST response resource type.
        :type type: GetAstResponseDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
