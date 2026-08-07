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
    from datadog_api_client.v2.model.create_degradation_request_data_attributes import (
        CreateDegradationRequestDataAttributes,
    )
    from datadog_api_client.v2.model.degradation_request_data_meta import DegradationRequestDataMeta
    from datadog_api_client.v2.model.create_degradation_request_data_relationships import (
        CreateDegradationRequestDataRelationships,
    )
    from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType


class CreateDegradationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_request_data_attributes import (
            CreateDegradationRequestDataAttributes,
        )
        from datadog_api_client.v2.model.degradation_request_data_meta import DegradationRequestDataMeta
        from datadog_api_client.v2.model.create_degradation_request_data_relationships import (
            CreateDegradationRequestDataRelationships,
        )
        from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType

        return {
            "attributes": (CreateDegradationRequestDataAttributes,),
            "meta": (DegradationRequestDataMeta,),
            "relationships": (CreateDegradationRequestDataRelationships,),
            "type": (PatchDegradationRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "meta": "meta",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: CreateDegradationRequestDataAttributes,
        type: PatchDegradationRequestDataType,
        meta: Union[DegradationRequestDataMeta, UnsetType] = unset,
        relationships: Union[CreateDegradationRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for creating a degradation.

        :param attributes: The supported attributes for creating a degradation.
        :type attributes: CreateDegradationRequestDataAttributes

        :param meta: The supported metadata for a degradation request.
        :type meta: DegradationRequestDataMeta, optional

        :param relationships: The supported relationships for creating a degradation.
        :type relationships: CreateDegradationRequestDataRelationships, optional

        :param type: Degradations resource type.
        :type type: PatchDegradationRequestDataType
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
