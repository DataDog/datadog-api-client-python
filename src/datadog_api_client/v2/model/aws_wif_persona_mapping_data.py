# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.aws_wif_persona_mapping_attributes import AwsWifPersonaMappingAttributes
    from datadog_api_client.v2.model.aws_wif_persona_mapping_type import AwsWifPersonaMappingType


class AwsWifPersonaMappingData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_wif_persona_mapping_attributes import AwsWifPersonaMappingAttributes
        from datadog_api_client.v2.model.aws_wif_persona_mapping_type import AwsWifPersonaMappingType

        return {
            "attributes": (AwsWifPersonaMappingAttributes,),
            "id": (UUID,),
            "type": (AwsWifPersonaMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AwsWifPersonaMappingAttributes, id: UUID, type: AwsWifPersonaMappingType, **kwargs):
        """
        An AWS WIF persona mapping resource.

        :param attributes: Attributes of an AWS WIF persona mapping.
        :type attributes: AwsWifPersonaMappingAttributes

        :param id: The UUID of the persona mapping.
        :type id: UUID

        :param type: Type identifier for an AWS WIF persona mapping.
        :type type: AwsWifPersonaMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
