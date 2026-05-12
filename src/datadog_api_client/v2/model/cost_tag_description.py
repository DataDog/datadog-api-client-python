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
    from datadog_api_client.v2.model.cost_tag_description_attributes import CostTagDescriptionAttributes
    from datadog_api_client.v2.model.cost_tag_description_type import CostTagDescriptionType


class CostTagDescription(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_description_attributes import CostTagDescriptionAttributes
        from datadog_api_client.v2.model.cost_tag_description_type import CostTagDescriptionType

        return {
            "attributes": (CostTagDescriptionAttributes,),
            "id": (str,),
            "type": (CostTagDescriptionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CostTagDescriptionAttributes, id: str, type: CostTagDescriptionType, **kwargs):
        """
        A Cloud Cost Management tag key description, either cross-cloud or scoped to a single cloud provider.

        :param attributes: Human-readable description and metadata attached to a Cloud Cost Management tag key, optionally scoped to a single cloud provider.
        :type attributes: CostTagDescriptionAttributes

        :param id: Stable identifier of the tag description. Equals the tag key when the description is the cross-cloud default; encodes both the cloud and the tag key when the description is cloud-specific.
        :type id: str

        :param type: Type of the Cloud Cost Management tag description resource.
        :type type: CostTagDescriptionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
