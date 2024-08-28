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
    from datadog_api_client.v2.model.entity_response_included_related_oncall_attributes import (
        EntityResponseIncludedRelatedOncallAttributes,
    )


class EntityResponseIncludedOncall(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_response_included_related_oncall_attributes import (
            EntityResponseIncludedRelatedOncallAttributes,
        )

        return {
            "attributes": (EntityResponseIncludedRelatedOncallAttributes,),
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
        attributes: Union[EntityResponseIncludedRelatedOncallAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Included oncall.

        :param attributes: Included related oncall attributes.
        :type attributes: EntityResponseIncludedRelatedOncallAttributes, optional

        :param id: Oncall ID.
        :type id: str, optional

        :param type: Oncall type.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
