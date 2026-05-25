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
    from datadog_api_client.v2.model.get_ast_request_data_attributes import GetAstRequestDataAttributes
    from datadog_api_client.v2.model.get_ast_request_data_type import GetAstRequestDataType


class GetAstRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_ast_request_data_attributes import GetAstRequestDataAttributes
        from datadog_api_client.v2.model.get_ast_request_data_type import GetAstRequestDataType

        return {
            "attributes": (GetAstRequestDataAttributes,),
            "id": (str,),
            "type": (GetAstRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: GetAstRequestDataAttributes,
        type: GetAstRequestDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The primary data object in the get-AST request.

        :param attributes: The attributes of the get-AST request, containing the source code to parse.
        :type attributes: GetAstRequestDataAttributes

        :param id: An optional identifier for the get-AST request resource.
        :type id: str, optional

        :param type: Get AST request resource type.
        :type type: GetAstRequestDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
