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
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_style_display_any_of_any_of_item_legend import (
        ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend,
    )
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_style_display_any_of_any_of_item_type import (
        ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType,
    )


class ToplistBackendDefinitionStyle20270101DisplayOneOf(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.toplist_backend_definition_style_display_any_of_any_of_item_legend import (
            ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend,
        )
        from datadog_api_client.v1_20270101.model.toplist_backend_definition_style_display_any_of_any_of_item_type import (
            ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType,
        )

        return {
            "legend": (ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend,),
            "type": (ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType,),
        }

    attribute_map = {
        "legend": "legend",
        "type": "type",
    }

    def __init__(
        self_,
        type: ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType,
        legend: Union[ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param legend: Test-only generated schema for the dashboard versioning proof of concept.
        :type legend: ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemLegend, optional

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType
        """
        if legend is not unset:
            kwargs["legend"] = legend
        super().__init__(kwargs)

        self_.type = type
