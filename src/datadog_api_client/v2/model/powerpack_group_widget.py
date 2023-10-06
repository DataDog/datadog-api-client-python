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
    from datadog_api_client.v2.model.powerpack_group_widget_definition import PowerpackGroupWidgetDefinition
    from datadog_api_client.v2.model.powerpack_group_widget_layout import PowerpackGroupWidgetLayout


class PowerpackGroupWidget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.powerpack_group_widget_definition import PowerpackGroupWidgetDefinition
        from datadog_api_client.v2.model.powerpack_group_widget_layout import PowerpackGroupWidgetLayout

        return {
            "definition": (PowerpackGroupWidgetDefinition,),
            "layout": (PowerpackGroupWidgetLayout,),
        }

    attribute_map = {
        "definition": "definition",
        "layout": "layout",
    }

    def __init__(
        self_,
        definition: PowerpackGroupWidgetDefinition,
        layout: Union[PowerpackGroupWidgetLayout, UnsetType] = unset,
        **kwargs,
    ):
        """
        Powerpack group widget definition object.

        :param definition: Powerpack group widget object.
        :type definition: PowerpackGroupWidgetDefinition

        :param layout: Powerpack group widget layout.
        :type layout: PowerpackGroupWidgetLayout, optional
        """
        if layout is not unset:
            kwargs["layout"] = layout
        super().__init__(kwargs)

        self_.definition = definition
