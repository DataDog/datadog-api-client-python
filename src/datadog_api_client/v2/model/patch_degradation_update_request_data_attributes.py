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
    from datadog_api_client.v2.model.patch_degradation_update_request_data_attributes_status import (
        PatchDegradationUpdateRequestDataAttributesStatus,
    )


class PatchDegradationUpdateRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_degradation_update_request_data_attributes_status import (
            PatchDegradationUpdateRequestDataAttributesStatus,
        )

        return {
            "description": (str,),
            "status": (PatchDegradationUpdateRequestDataAttributesStatus,),
        }

    attribute_map = {
        "description": "description",
        "status": "status",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        status: Union[PatchDegradationUpdateRequestDataAttributesStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for editing a degradation update.

        :param description: The message body of the update.
        :type description: str, optional

        :param status: The status of the degradation update.
        :type status: PatchDegradationUpdateRequestDataAttributesStatus, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
