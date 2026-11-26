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
    from datadog_api_client.v1_20270101.model.toplist_backend_definition_style_display_any_of_any_of_item_type4453028448 import (
        ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType4453028448,
    )


class ToplistBackendDefinitionStyle20270101DisplayOneOf4453175744(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.toplist_backend_definition_style_display_any_of_any_of_item_type4453028448 import (
            ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType4453028448,
        )

        return {
            "type": (ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType4453028448,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType4453028448, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: ToplistBackendDefinitionStyleDisplayAnyOfAnyOfItemType4453028448
        """
        super().__init__(kwargs)

        self_.type = type
