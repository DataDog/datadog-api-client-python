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
    from datadog_api_client.v2.model.entity_response_included_raw_schema_attributes import (
        EntityResponseIncludedRawSchemaAttributes,
    )


class EntityResponseIncludedRawSchema(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_response_included_raw_schema_attributes import (
            EntityResponseIncludedRawSchemaAttributes,
        )

        return {
            "attributes": (EntityResponseIncludedRawSchemaAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[EntityResponseIncludedRawSchemaAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Included raw schema.

        :param attributes: Included raw schema attributes.
        :type attributes: EntityResponseIncludedRawSchemaAttributes, optional

        :param id: Raw schema id.
        :type id: str, optional

        :param type: Raw schema type.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
