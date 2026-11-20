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
    from datadog_api_client.v1_20270101.model.image_backend_definition_horizontal_align import (
        ImageBackendDefinitionHorizontalAlign,
    )
    from datadog_api_client.v1_20270101.model.image_margin import ImageMargin
    from datadog_api_client.v1_20270101.model.image_backend_definition20270101_sizing import (
        ImageBackendDefinition20270101Sizing,
    )
    from datadog_api_client.v1_20270101.model.image_backend_definition_type import ImageBackendDefinitionType
    from datadog_api_client.v1_20270101.model.image_backend_definition_vertical_align import (
        ImageBackendDefinitionVerticalAlign,
    )


class ImageBackendDefinition(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.image_backend_definition_horizontal_align import (
            ImageBackendDefinitionHorizontalAlign,
        )
        from datadog_api_client.v1_20270101.model.image_margin import ImageMargin
        from datadog_api_client.v1_20270101.model.image_backend_definition20270101_sizing import (
            ImageBackendDefinition20270101Sizing,
        )
        from datadog_api_client.v1_20270101.model.image_backend_definition_type import ImageBackendDefinitionType
        from datadog_api_client.v1_20270101.model.image_backend_definition_vertical_align import (
            ImageBackendDefinitionVerticalAlign,
        )

        return {
            "caption": (str,),
            "has_background": (bool,),
            "has_border": (bool,),
            "horizontal_align": (ImageBackendDefinitionHorizontalAlign,),
            "margin": (ImageMargin,),
            "sizing": (ImageBackendDefinition20270101Sizing,),
            "type": (ImageBackendDefinitionType,),
            "url": (str,),
            "url_dark_theme": (str,),
            "vertical_align": (ImageBackendDefinitionVerticalAlign,),
        }

    attribute_map = {
        "caption": "caption",
        "has_background": "has_background",
        "has_border": "has_border",
        "horizontal_align": "horizontal_align",
        "margin": "margin",
        "sizing": "sizing",
        "type": "type",
        "url": "url",
        "url_dark_theme": "url_dark_theme",
        "vertical_align": "vertical_align",
    }

    def __init__(
        self_,
        type: ImageBackendDefinitionType,
        url: str,
        caption: Union[str, UnsetType] = unset,
        has_background: Union[bool, UnsetType] = unset,
        has_border: Union[bool, UnsetType] = unset,
        horizontal_align: Union[ImageBackendDefinitionHorizontalAlign, UnsetType] = unset,
        margin: Union[ImageMargin, UnsetType] = unset,
        sizing: Union[ImageBackendDefinition20270101Sizing, float, str, UnsetType] = unset,
        url_dark_theme: Union[str, UnsetType] = unset,
        vertical_align: Union[ImageBackendDefinitionVerticalAlign, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param caption: Test-only generated schema for the dashboard versioning proof of concept.
        :type caption: str, optional

        :param has_background: Test-only generated schema for the dashboard versioning proof of concept.
        :type has_background: bool, optional

        :param has_border: Test-only generated schema for the dashboard versioning proof of concept.
        :type has_border: bool, optional

        :param horizontal_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type horizontal_align: ImageBackendDefinitionHorizontalAlign, optional

        :param margin: Test-only generated schema for the dashboard versioning proof of concept.
        :type margin: ImageMargin, optional

        :param sizing: Test-only generated schema for the dashboard versioning proof of concept.
        :type sizing: ImageBackendDefinition20270101Sizing, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ImageBackendDefinitionType

        :param url: Test-only generated schema for the dashboard versioning proof of concept.
        :type url: str

        :param url_dark_theme: Test-only generated schema for the dashboard versioning proof of concept.
        :type url_dark_theme: str, optional

        :param vertical_align: Test-only generated schema for the dashboard versioning proof of concept.
        :type vertical_align: ImageBackendDefinitionVerticalAlign, optional
        """
        if caption is not unset:
            kwargs["caption"] = caption
        if has_background is not unset:
            kwargs["has_background"] = has_background
        if has_border is not unset:
            kwargs["has_border"] = has_border
        if horizontal_align is not unset:
            kwargs["horizontal_align"] = horizontal_align
        if margin is not unset:
            kwargs["margin"] = margin
        if sizing is not unset:
            kwargs["sizing"] = sizing
        if url_dark_theme is not unset:
            kwargs["url_dark_theme"] = url_dark_theme
        if vertical_align is not unset:
            kwargs["vertical_align"] = vertical_align
        super().__init__(kwargs)

        self_.type = type
        self_.url = url
