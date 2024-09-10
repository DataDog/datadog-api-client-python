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
    from datadog_api_client.v2.model.asm_exclusion_filter_update_attributes import ASMExclusionFilterUpdateAttributes
    from datadog_api_client.v2.model.asm_exclusion_filter_type import ASMExclusionFilterType


class ASMExclusionFilterUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asm_exclusion_filter_update_attributes import (
            ASMExclusionFilterUpdateAttributes,
        )
        from datadog_api_client.v2.model.asm_exclusion_filter_type import ASMExclusionFilterType

        return {
            "attributes": (ASMExclusionFilterUpdateAttributes,),
            "id": (str,),
            "type": (ASMExclusionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ASMExclusionFilterUpdateAttributes,
        type: ASMExclusionFilterType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single Exclusion filter.

        :param attributes: Update an existing ASM Exclusion filter.
        :type attributes: ASMExclusionFilterUpdateAttributes

        :param id: The ID of the exclusion filter.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``exclusion_filter``.
        :type type: ASMExclusionFilterType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
