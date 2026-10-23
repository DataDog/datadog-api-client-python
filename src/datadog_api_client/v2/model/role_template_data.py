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
    from datadog_api_client.v2.model.role_template_data_attributes import RoleTemplateDataAttributes
    from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
    from datadog_api_client.v2.model.role_template_data_type import RoleTemplateDataType


class RoleTemplateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.role_template_data_attributes import RoleTemplateDataAttributes
        from datadog_api_client.v2.model.role_response_relationships import RoleResponseRelationships
        from datadog_api_client.v2.model.role_template_data_type import RoleTemplateDataType

        return {
            "attributes": (RoleTemplateDataAttributes,),
            "id": (str,),
            "relationships": (RoleResponseRelationships,),
            "type": (RoleTemplateDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: RoleTemplateDataType,
        attributes: Union[RoleTemplateDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[RoleResponseRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``RoleTemplateData`` object.

        :param attributes: The definition of ``RoleTemplateDataAttributes`` object.
        :type attributes: RoleTemplateDataAttributes, optional

        :param id: The ``RoleTemplateData`` ``id``.
        :type id: str, optional

        :param relationships: Relationships of the role object returned by the API.
        :type relationships: RoleResponseRelationships, optional

        :param type: Roles resource type.
        :type type: RoleTemplateDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
