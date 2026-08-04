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
    from datadog_api_client.v2.model.create_backfilled_degradation_request_data_attributes import (
        CreateBackfilledDegradationRequestDataAttributes,
    )
    from datadog_api_client.v2.model.create_backfilled_degradation_request_data_relationships import (
        CreateBackfilledDegradationRequestDataRelationships,
    )
    from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType


class CreateBackfilledDegradationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_backfilled_degradation_request_data_attributes import (
            CreateBackfilledDegradationRequestDataAttributes,
        )
        from datadog_api_client.v2.model.create_backfilled_degradation_request_data_relationships import (
            CreateBackfilledDegradationRequestDataRelationships,
        )
        from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType

        return {
            "attributes": (CreateBackfilledDegradationRequestDataAttributes,),
            "relationships": (CreateBackfilledDegradationRequestDataRelationships,),
            "type": (PatchDegradationRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchDegradationRequestDataType,
        attributes: Union[CreateBackfilledDegradationRequestDataAttributes, UnsetType] = unset,
        relationships: Union[CreateBackfilledDegradationRequestDataRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for creating a backfilled degradation.

        :param attributes: The supported attributes for creating a backfilled degradation.
        :type attributes: CreateBackfilledDegradationRequestDataAttributes, optional

        :param relationships: The supported relationships for creating a backfilled degradation.
        :type relationships: CreateBackfilledDegradationRequestDataRelationships, optional

        :param type: Degradations resource type.
        :type type: PatchDegradationRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.type = type
