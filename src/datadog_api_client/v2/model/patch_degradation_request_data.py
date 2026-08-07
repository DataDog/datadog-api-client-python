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
    from datadog_api_client.v2.model.patch_degradation_request_data_attributes import (
        PatchDegradationRequestDataAttributes,
    )
    from datadog_api_client.v2.model.degradation_request_data_meta import DegradationRequestDataMeta
    from datadog_api_client.v2.model.patch_degradation_request_data_relationships import (
        PatchDegradationRequestDataRelationships,
    )
    from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType


class PatchDegradationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_degradation_request_data_attributes import (
            PatchDegradationRequestDataAttributes,
        )
        from datadog_api_client.v2.model.degradation_request_data_meta import DegradationRequestDataMeta
        from datadog_api_client.v2.model.patch_degradation_request_data_relationships import (
            PatchDegradationRequestDataRelationships,
        )
        from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType

        return {
            "attributes": (PatchDegradationRequestDataAttributes,),
            "id": (UUID,),
            "meta": (DegradationRequestDataMeta,),
            "relationships": (PatchDegradationRequestDataRelationships,),
            "type": (PatchDegradationRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: PatchDegradationRequestDataAttributes,
        id: UUID,
        type: PatchDegradationRequestDataType,
        meta: Union[DegradationRequestDataMeta, UnsetType] = unset,
        relationships: Union[PatchDegradationRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for updating a degradation.

        :param attributes: The supported attributes for updating a degradation.
        :type attributes: PatchDegradationRequestDataAttributes

        :param id: The ID of the degradation.
        :type id: UUID

        :param meta: The supported metadata for a degradation request.
        :type meta: DegradationRequestDataMeta, optional

        :param relationships: The supported relationships for updating a degradation.
        :type relationships: PatchDegradationRequestDataRelationships, optional

        :param type: Degradations resource type.
        :type type: PatchDegradationRequestDataType
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
