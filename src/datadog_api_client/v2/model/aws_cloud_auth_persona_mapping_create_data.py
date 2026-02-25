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
    from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_create_attributes import (
        AWSCloudAuthPersonaMappingCreateAttributes,
    )
    from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_type import AWSCloudAuthPersonaMappingType


class AWSCloudAuthPersonaMappingCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_create_attributes import (
            AWSCloudAuthPersonaMappingCreateAttributes,
        )
        from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_type import AWSCloudAuthPersonaMappingType

        return {
            "attributes": (AWSCloudAuthPersonaMappingCreateAttributes,),
            "type": (AWSCloudAuthPersonaMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: AWSCloudAuthPersonaMappingCreateAttributes, type: AWSCloudAuthPersonaMappingType, **kwargs
    ):
        """
        Data for creating an AWS cloud authentication persona mapping

        :param attributes: Attributes for creating an AWS cloud authentication persona mapping
        :type attributes: AWSCloudAuthPersonaMappingCreateAttributes

        :param type: Type identifier for AWS cloud authentication persona mapping
        :type type: AWSCloudAuthPersonaMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
