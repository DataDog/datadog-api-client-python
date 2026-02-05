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
    from datadog_api_client.v2.model.postmortem_template_attributes_response import PostmortemTemplateAttributesResponse
    from datadog_api_client.v2.model.postmortem_template_type import PostmortemTemplateType


class PostmortemTemplateDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_template_attributes_response import (
            PostmortemTemplateAttributesResponse,
        )
        from datadog_api_client.v2.model.postmortem_template_type import PostmortemTemplateType

        return {
            "attributes": (PostmortemTemplateAttributesResponse,),
            "id": (str,),
            "type": (PostmortemTemplateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: PostmortemTemplateAttributesResponse, id: str, type: PostmortemTemplateType, **kwargs
    ):
        """


        :param attributes:
        :type attributes: PostmortemTemplateAttributesResponse

        :param id: The ID of the template
        :type id: str

        :param type: Postmortem template resource type
        :type type: PostmortemTemplateType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
