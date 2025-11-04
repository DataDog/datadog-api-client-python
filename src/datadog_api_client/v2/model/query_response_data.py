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
    from datadog_api_client.v2.model.query_response_data_attributes import QueryResponseDataAttributes
    from datadog_api_client.v2.model.query_response_data_type import QueryResponseDataType


class QueryResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.query_response_data_attributes import QueryResponseDataAttributes
        from datadog_api_client.v2.model.query_response_data_type import QueryResponseDataType

        return {
            "attributes": (QueryResponseDataAttributes,),
            "id": (str,),
            "type": (QueryResponseDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: QueryResponseDataType,
        attributes: Union[QueryResponseDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: QueryResponseDataAttributes, optional

        :param id:
        :type id: str, optional

        :param type: Query response resource type.
        :type type: QueryResponseDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
