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
    from datadog_api_client.v2.model.patch_maintenance_update_request_data import PatchMaintenanceUpdateRequestData


class PatchMaintenanceUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_maintenance_update_request_data import PatchMaintenanceUpdateRequestData

        return {
            "data": (PatchMaintenanceUpdateRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[PatchMaintenanceUpdateRequestData, UnsetType] = unset, **kwargs):
        """
        Request object for editing a maintenance update.

        :param data: The data object for editing a maintenance update.
        :type data: PatchMaintenanceUpdateRequestData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
