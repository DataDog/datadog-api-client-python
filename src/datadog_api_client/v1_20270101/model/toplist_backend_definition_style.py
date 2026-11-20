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
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_style20270101_display import (
        ToplistBackendDefinitionStyle20270101Display,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_style_scaling import (
        ToplistBackendDefinitionStyleScaling,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_style20270101_display_one_of import (
        ToplistBackendDefinitionStyle20270101DisplayOneOf,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_style20270101_display_one_of4453175744 import (
        ToplistBackendDefinitionStyle20270101DisplayOneOf4453175744,
    )


class ToplistBackendDefinitionStyle(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.toplist_backend_definition_style20270101_display import (
            ToplistBackendDefinitionStyle20270101Display,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_definition_style_scaling import (
            ToplistBackendDefinitionStyleScaling,
        )

        return {
            "display": (ToplistBackendDefinitionStyle20270101Display,),
            "palette": (str,),
            "scaling": (ToplistBackendDefinitionStyleScaling,),
        }

    attribute_map = {
        "display": "display",
        "palette": "palette",
        "scaling": "scaling",
    }

    def __init__(
        self_,
        display: Union[
            ToplistBackendDefinitionStyle20270101Display,
            ToplistBackendDefinitionStyle20270101DisplayOneOf,
            ToplistBackendDefinitionStyle20270101DisplayOneOf4453175744,
            UnsetType,
        ] = unset,
        palette: Union[str, UnsetType] = unset,
        scaling: Union[ToplistBackendDefinitionStyleScaling, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param display: Test-only generated schema for the dashboard versioning proof of concept.
        :type display: ToplistBackendDefinitionStyle20270101Display, optional

        :param palette: Test-only generated schema for the dashboard versioning proof of concept.
        :type palette: str, optional

        :param scaling: Test-only generated schema for the dashboard versioning proof of concept.
        :type scaling: ToplistBackendDefinitionStyleScaling, optional
        """
        if display is not unset:
            kwargs["display"] = display
        if palette is not unset:
            kwargs["palette"] = palette
        if scaling is not unset:
            kwargs["scaling"] = scaling
        super().__init__(kwargs)
