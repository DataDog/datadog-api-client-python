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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.list_apis_response_data_attributes import ListAPIsResponseDataAttributes


class ListAPIsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_apis_response_data_attributes import ListAPIsResponseDataAttributes

        return {
            "attributes": (ListAPIsResponseDataAttributes,),
            "id": (UUID,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
    }

    def __init__(
        self_,
        attributes: Union[ListAPIsResponseDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data envelope for ``ListAPIsResponse``.

        :param attributes: Attributes for ``ListAPIsResponseData``.
        :type attributes: ListAPIsResponseDataAttributes, optional

        :param id: API identifier.
        :type id: UUID, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)
