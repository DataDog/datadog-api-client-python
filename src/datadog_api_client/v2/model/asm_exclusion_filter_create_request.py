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
    from datadog_api_client.v2.model.asm_exclusion_filter_create_data import ASMExclusionFilterCreateData


class ASMExclusionFilterCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asm_exclusion_filter_create_data import ASMExclusionFilterCreateData

        return {
            "data": (ASMExclusionFilterCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: ASMExclusionFilterCreateData, **kwargs):
        """
        Request object that includes the exclusion filter to create.

        :param data: Object for a single exclusion filter.
        :type data: ASMExclusionFilterCreateData
        """
        super().__init__(kwargs)

        self_.data = data
