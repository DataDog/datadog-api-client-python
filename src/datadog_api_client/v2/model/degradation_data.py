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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.degradation_data_attributes import DegradationDataAttributes
    from datadog_api_client.v2.model.degradation_data_relationships import DegradationDataRelationships
    from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType


class DegradationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_data_attributes import DegradationDataAttributes
        from datadog_api_client.v2.model.degradation_data_relationships import DegradationDataRelationships
        from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType

        return {
            "attributes": (DegradationDataAttributes,),
            "id": (UUID,),
            "relationships": (DegradationDataRelationships,),
            "type": (PatchDegradationRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchDegradationRequestDataType,
        attributes: Union[DegradationDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        relationships: Union[DegradationDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: The attributes of a degradation.
        :type attributes: DegradationDataAttributes, optional

        :param id: The ID of the degradation.
        :type id: UUID, optional

        :param relationships: The relationships of a degradation.
        :type relationships: DegradationDataRelationships, optional

        :param type: Degradations resource type.
        :type type: PatchDegradationRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
