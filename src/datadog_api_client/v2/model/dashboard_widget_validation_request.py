# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dashboard_widget_validation_layout_type import DashboardWidgetValidationLayoutType
    from datadog_api_client.v2.model.dashboard_widget_validation_reflow_type import DashboardWidgetValidationReflowType
    from datadog_api_client.v2.model.dashboard_widget_validation_widget import DashboardWidgetValidationWidget


class DashboardWidgetValidationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dashboard_widget_validation_layout_type import (
            DashboardWidgetValidationLayoutType,
        )
        from datadog_api_client.v2.model.dashboard_widget_validation_reflow_type import (
            DashboardWidgetValidationReflowType,
        )
        from datadog_api_client.v2.model.dashboard_widget_validation_widget import DashboardWidgetValidationWidget

        return {
            "layout_type": (DashboardWidgetValidationLayoutType,),
            "reflow_type": (DashboardWidgetValidationReflowType,),
            "widgets": ([DashboardWidgetValidationWidget],),
        }

    attribute_map = {
        "layout_type": "layout_type",
        "reflow_type": "reflow_type",
        "widgets": "widgets",
    }

    def __init__(
        self_,
        layout_type: DashboardWidgetValidationLayoutType,
        widgets: List[DashboardWidgetValidationWidget],
        reflow_type: Union[DashboardWidgetValidationReflowType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request containing dashboard widgets and their layout context.

        :param layout_type: Layout type used to apply dashboard-specific widget layout validation.
        :type layout_type: DashboardWidgetValidationLayoutType

        :param reflow_type: Reflow behavior used for an ordered dashboard.
        :type reflow_type: DashboardWidgetValidationReflowType, optional

        :param widgets: Dashboard widgets to validate.
        :type widgets: [DashboardWidgetValidationWidget]
        """
        if reflow_type is not unset:
            kwargs["reflow_type"] = reflow_type
        super().__init__(kwargs)

        self_.layout_type = layout_type
        self_.widgets = widgets
