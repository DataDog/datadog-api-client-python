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
    from datadog_api_client.v2.model.create_degradation_request_data_attributes import (
        CreateDegradationRequestDataAttributes,
    )
    from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType


class CreateDegradationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_request_data_attributes import (
            CreateDegradationRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType

        return {
            "attributes": (CreateDegradationRequestDataAttributes,),
            "type": (PatchDegradationRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: CreateDegradationRequestDataAttributes, type: PatchDegradationRequestDataType, **kwargs
    ):
        """


        :param attributes: The supported attributes for creating a degradation.
        :type attributes: CreateDegradationRequestDataAttributes

        :param type: Degradations resource type.
        :type type: PatchDegradationRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
