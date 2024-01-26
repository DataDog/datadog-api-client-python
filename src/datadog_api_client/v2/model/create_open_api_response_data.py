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
    from datadog_api_client.v2.model.create_open_api_response_attributes import CreateOpenAPIResponseAttributes


class CreateOpenAPIResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_open_api_response_attributes import CreateOpenAPIResponseAttributes

        return {
            "attributes": (CreateOpenAPIResponseAttributes,),
            "id": (UUID,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
    }

    def __init__(
        self_,
        attributes: Union[CreateOpenAPIResponseAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data envelope for ``CreateOpenAPIResponse``.

        :param attributes: Attributes for ``CreateOpenAPI``.
        :type attributes: CreateOpenAPIResponseAttributes, optional

        :param id: API identifier.
        :type id: UUID, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)
