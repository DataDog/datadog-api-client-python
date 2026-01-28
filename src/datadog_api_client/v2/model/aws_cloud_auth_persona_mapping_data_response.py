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
    from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_attributes_response import (
        AWSCloudAuthPersonaMappingAttributesResponse,
    )
    from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_type import AWSCloudAuthPersonaMappingType


class AWSCloudAuthPersonaMappingDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_attributes_response import (
            AWSCloudAuthPersonaMappingAttributesResponse,
        )
        from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_type import AWSCloudAuthPersonaMappingType

        return {
            "attributes": (AWSCloudAuthPersonaMappingAttributesResponse,),
            "id": (str,),
            "type": (AWSCloudAuthPersonaMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: AWSCloudAuthPersonaMappingAttributesResponse,
        id: str,
        type: AWSCloudAuthPersonaMappingType,
        **kwargs,
    ):
        """
        Data for AWS cloud authentication persona mapping response

        :param attributes: Attributes for AWS cloud authentication persona mapping response
        :type attributes: AWSCloudAuthPersonaMappingAttributesResponse

        :param id: Unique identifier for the persona mapping
        :type id: str

        :param type: Type identifier for AWS cloud authentication persona mapping
        :type type: AWSCloudAuthPersonaMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
