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
    from datadog_api_client.v2.model.patch_saved_filter_data import PatchSavedFilterData


class PatchSavedFilterRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.patch_saved_filter_data import PatchSavedFilterData

        return {
            "data": (PatchSavedFilterData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: PatchSavedFilterData, **kwargs):
        """
        Request to partially update a saved filter.

        :param data: The saved filter fields to update.
        :type data: PatchSavedFilterData
        """
        super().__init__(kwargs)

        self_.data = data
