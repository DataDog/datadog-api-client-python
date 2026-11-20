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
    from datadog_api_client.v1_20270101.model.check_status_backend_definition import CheckStatusBackendDefinition
    from datadog_api_client.v1_20270101.model.widget_layout import WidgetLayout
    from datadog_api_client.v1_20270101.model.free_layout import FreeLayout
    from datadog_api_client.v1_20270101.model.msl_widget_layout import MSLWidgetLayout
    from datadog_api_client.v1_20270101.model.msl_backend_widget_layout import MSLBackendWidgetLayout


class CheckStatusBackendWidget(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.check_status_backend_definition import CheckStatusBackendDefinition
        from datadog_api_client.v1_20270101.model.widget_layout import WidgetLayout

        return {
            "definition": (CheckStatusBackendDefinition,),
            "id": (float,),
            "layout": (WidgetLayout,),
        }

    attribute_map = {
        "definition": "definition",
        "id": "id",
        "layout": "layout",
    }

    def __init__(
        self_,
        definition: CheckStatusBackendDefinition,
        id: Union[float, UnsetType] = unset,
        layout: Union[WidgetLayout, FreeLayout, MSLWidgetLayout, MSLBackendWidgetLayout, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param definition: Test-only generated schema for the dashboard versioning proof of concept.
        :type definition: CheckStatusBackendDefinition

        :param id: Test-only generated schema for the dashboard versioning proof of concept.
        :type id: float, optional

        :param layout: Test-only generated schema for the dashboard versioning proof of concept.
        :type layout: WidgetLayout, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if layout is not unset:
            kwargs["layout"] = layout
        super().__init__(kwargs)

        self_.definition = definition
