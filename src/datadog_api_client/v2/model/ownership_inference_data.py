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
    from datadog_api_client.v2.model.ownership_inference_attributes import OwnershipInferenceAttributes
    from datadog_api_client.v2.model.ownership_inference_type import OwnershipInferenceType


class OwnershipInferenceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ownership_inference_attributes import OwnershipInferenceAttributes
        from datadog_api_client.v2.model.ownership_inference_type import OwnershipInferenceType

        return {
            "attributes": (OwnershipInferenceAttributes,),
            "id": (str,),
            "type": (OwnershipInferenceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: OwnershipInferenceAttributes, id: str, type: OwnershipInferenceType, **kwargs):
        """
        The data wrapper for a single ownership inference response.

        :param attributes: The attributes of a single ownership inference.
        :type attributes: OwnershipInferenceAttributes

        :param id: The identifier of the inference, formatted as ``resource_id:owner_type``.
        :type id: str

        :param type: The type of the ownership inference resource. The value should always be ``ownership_inference``.
        :type type: OwnershipInferenceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
