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
    from datadog_api_client.v2.model.ownership_inference_list_attributes import OwnershipInferenceListAttributes
    from datadog_api_client.v2.model.ownership_inferences_type import OwnershipInferencesType


class OwnershipInferenceListData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_inference_list_attributes import OwnershipInferenceListAttributes
        from datadog_api_client.v2.model.ownership_inferences_type import OwnershipInferencesType

        return {
            "attributes": (OwnershipInferenceListAttributes,),
            "id": (str,),
            "type": (OwnershipInferencesType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OwnershipInferenceListAttributes, id: str, type: OwnershipInferencesType, **kwargs):
        """
        The data wrapper for the ownership inferences collection response.

        :param attributes: The attributes of the ownership inferences collection response.
        :type attributes: OwnershipInferenceListAttributes

        :param id: The resource identifier associated with the returned inferences.
        :type id: str

        :param type: The type of the ownership inferences collection resource. The value should always be ``ownership_inferences``.
        :type type: OwnershipInferencesType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
