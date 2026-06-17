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
    from datadog_api_client.v2.model.aws_wif_intake_mapping_attributes import AwsWifIntakeMappingAttributes
    from datadog_api_client.v2.model.aws_wif_intake_mapping_type import AwsWifIntakeMappingType


class AwsWifIntakeMappingData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.aws_wif_intake_mapping_attributes import AwsWifIntakeMappingAttributes
        from datadog_api_client.v2.model.aws_wif_intake_mapping_type import AwsWifIntakeMappingType

        return {
            "attributes": (AwsWifIntakeMappingAttributes,),
            "id": (UUID,),
            "type": (AwsWifIntakeMappingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: AwsWifIntakeMappingAttributes, id: UUID, type: AwsWifIntakeMappingType, **kwargs):
        """
        An AWS WIF intake mapping resource.

        :param attributes: Attributes of an AWS WIF intake mapping.
        :type attributes: AwsWifIntakeMappingAttributes

        :param id: The UUID of the intake mapping.
        :type id: UUID

        :param type: Type identifier for an AWS WIF intake mapping.
        :type type: AwsWifIntakeMappingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
