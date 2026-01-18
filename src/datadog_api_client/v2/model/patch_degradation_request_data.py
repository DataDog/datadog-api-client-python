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
    from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType


class PatchDegradationRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_degradation_request_data_attributes import (
            PatchDegradationRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_degradation_request_data_type import PatchDegradationRequestDataType

        return {
            "attributes": (PatchDegradationRequestDataAttributes,),
            "id": (UUID,),
            "type": (PatchDegradationRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchDegradationRequestDataType,
        attributes: Union[PatchDegradationRequestDataAttributes, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes: The supported attributes for updating a degradation.
        :type attributes: PatchDegradationRequestDataAttributes, optional

        :param id: The ID of the degradation.
        :type id: UUID, optional

        :param type: Degradations resource type.
        :type type: PatchDegradationRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
