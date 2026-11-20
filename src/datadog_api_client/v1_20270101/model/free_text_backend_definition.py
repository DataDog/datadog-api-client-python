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
    from datadog_api_client.v1_20270101.model.free_text_backend_definition_text_align import (
        FreeTextBackendDefinitionTextAlign,
    )
    from datadog_api_client.v1_20270101.model.free_text_backend_definition_type import FreeTextBackendDefinitionType


class FreeTextBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.free_text_backend_definition_text_align import (
            FreeTextBackendDefinitionTextAlign,
        )
        from datadog_api_client.v1_20270101.model.free_text_backend_definition_type import FreeTextBackendDefinitionType

        return {
            "color": (str,),
            "font_size": (str,),
            "text": (str,),
            "text_align": (FreeTextBackendDefinitionTextAlign,),
            "type": (FreeTextBackendDefinitionType,),
        }

    attribute_map = {
        "color": "color",
        "font_size": "font_size",
        "text": "text",
        "text_align": "text_align",
        "type": "type",
    }

    def __init__(
        self_,
        text: str,
        type: FreeTextBackendDefinitionType,
        color: Union[str, UnsetType] = unset,
        font_size: Union[str, UnsetType] = unset,
        text_align: Union[FreeTextBackendDefinitionTextAlign, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param color: Test-only generated schema for the dashboard versioning proof of concept.
        :type color: str, optional

        :param font_size: Test-only generated schema for the dashboard versioning proof of concept.
        :type font_size: str, optional

        :param text: Test-only generated schema for the dashboard versioning proof of concept.
        :type text: str

        :param text_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type text_align: FreeTextBackendDefinitionTextAlign, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: FreeTextBackendDefinitionType
        """
        if color is not unset:
            kwargs["color"] = color
        if font_size is not unset:
            kwargs["font_size"] = font_size
        if text_align is not unset:
            kwargs["text_align"] = text_align
        super().__init__(kwargs)

        self_.text = text
        self_.type = type
