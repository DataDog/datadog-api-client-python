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
    from datadog_api_client.v2.model.postmortem_template_attributes_request import PostmortemTemplateAttributesRequest
    from datadog_api_client.v2.model.postmortem_template_create_relationships import (
        PostmortemTemplateCreateRelationships,
    )
    from datadog_api_client.v2.model.postmortem_template_type import PostmortemTemplateType


class PostmortemTemplateDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_template_attributes_request import (
            PostmortemTemplateAttributesRequest,
        )
        from datadog_api_client.v2.model.postmortem_template_create_relationships import (
            PostmortemTemplateCreateRelationships,
        )
        from datadog_api_client.v2.model.postmortem_template_type import PostmortemTemplateType

        return {
            "attributes": (PostmortemTemplateAttributesRequest,),
            "id": (str,),
            "relationships": (PostmortemTemplateCreateRelationships,),
            "type": (PostmortemTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: PostmortemTemplateAttributesRequest,
        type: PostmortemTemplateType,
        id: Union[str, UnsetType] = unset,
        relationships: Union[PostmortemTemplateCreateRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for creating or updating a postmortem template.

        :param attributes: Attributes for creating or updating a postmortem template.
        :type attributes: PostmortemTemplateAttributesRequest

        :param id: The ID of the template. Required when updating.
        :type id: str, optional

        :param relationships: Relationships for a postmortem template. ``incident_type`` is required when creating a template and is immutable afterwards.
        :type relationships: PostmortemTemplateCreateRelationships, optional

        :param type: Postmortem template resource type.
        :type type: PostmortemTemplateType
        """
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
