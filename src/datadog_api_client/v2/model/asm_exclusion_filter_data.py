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
    from datadog_api_client.v2.model.asm_exclusion_filter_attributes import ASMExclusionFilterAttributes
    from datadog_api_client.v2.model.asm_exclusion_filter_type import ASMExclusionFilterType


class ASMExclusionFilterData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asm_exclusion_filter_attributes import ASMExclusionFilterAttributes
        from datadog_api_client.v2.model.asm_exclusion_filter_type import ASMExclusionFilterType

        return {
            "attributes": (ASMExclusionFilterAttributes,),
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
        attributes: Union[ASMExclusionFilterAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ASMExclusionFilterType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object for a single Exclusion filter.

        :param attributes: The attributes of the ASM WAF exclusion filter.
        :type attributes: ASMExclusionFilterAttributes, optional

        :param id: The ID of the Exclusion filter.
        :type id: str, optional

        :param type: The type of the resource. The value should always be ``exclusion_filter``.
        :type type: ASMExclusionFilterType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
