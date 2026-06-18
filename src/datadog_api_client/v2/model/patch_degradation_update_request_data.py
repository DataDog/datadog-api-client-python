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
    from datadog_api_client.v2.model.patch_degradation_update_request_data_attributes import (
        PatchDegradationUpdateRequestDataAttributes,
    )
    from datadog_api_client.v2.model.patch_degradation_update_request_data_type import (
        PatchDegradationUpdateRequestDataType,
    )


class PatchDegradationUpdateRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_degradation_update_request_data_attributes import (
            PatchDegradationUpdateRequestDataAttributes,
        )
        from datadog_api_client.v2.model.patch_degradation_update_request_data_type import (
            PatchDegradationUpdateRequestDataType,
        )

        return {
            "attributes": (PatchDegradationUpdateRequestDataAttributes,),
            "id": (str,),
            "type": (PatchDegradationUpdateRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: PatchDegradationUpdateRequestDataType,
        attributes: Union[PatchDegradationUpdateRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The data object for editing a degradation update.

        :param attributes: Attributes for editing a degradation update.
        :type attributes: PatchDegradationUpdateRequestDataAttributes, optional

        :param id: The ID of the degradation update to edit.
        :type id: str, optional

        :param type: Degradation updates resource type.
        :type type: PatchDegradationUpdateRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
