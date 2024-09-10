# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.asm_exclusion_filter_type import ASMExclusionFilterType


class ASMExclusionFilterCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asm_exclusion_filter_type import ASMExclusionFilterType

        return {
            "attributes": (
                bool,
                date,
                datetime,
                dict,
                float,
                int,
                list,
                str,
                UUID,
                none_type,
            ),
            "type": (ASMExclusionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: Any, type: ASMExclusionFilterType, **kwargs):
        """
        Object for a single exclusion filter.

        :param attributes: Create a new ASM WAF exclusion filter.
        :type attributes: bool, date, datetime, dict, float, int, list, str, UUID, none_type

        :param type: The type of the resource. The value should always be ``exclusion_filter``.
        :type type: ASMExclusionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
