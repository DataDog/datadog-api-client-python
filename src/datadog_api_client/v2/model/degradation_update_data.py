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
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.degradation_update_data_attributes import DegradationUpdateDataAttributes
    from datadog_api_client.v2.model.degradation_update_data_relationships import DegradationUpdateDataRelationships
    from datadog_api_client.v2.model.patch_degradation_update_request_data_type import (
        PatchDegradationUpdateRequestDataType,
    )


class DegradationUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_update_data_attributes import DegradationUpdateDataAttributes
        from datadog_api_client.v2.model.degradation_update_data_relationships import DegradationUpdateDataRelationships
        from datadog_api_client.v2.model.patch_degradation_update_request_data_type import (
            PatchDegradationUpdateRequestDataType,
        )

        return {
            "attributes": (DegradationUpdateDataAttributes,),
            "id": (str,),
            "relationships": (DegradationUpdateDataRelationships,),
            "type": (PatchDegradationUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchDegradationUpdateRequestDataType,
        attributes: Union[DegradationUpdateDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[DegradationUpdateDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for a degradation update.

        :param attributes: Attributes of a degradation update resource.
        :type attributes: DegradationUpdateDataAttributes, optional

        :param id: The ID of the degradation update.
        :type id: str, optional

        :param relationships: Relationships of a degradation update resource.
        :type relationships: DegradationUpdateDataRelationships, optional

        :param type: Degradation updates resource type.
        :type type: PatchDegradationUpdateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
