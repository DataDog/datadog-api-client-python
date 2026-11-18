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
    from datadog_api_client.v2.model.product_analytics_launch_dashboard_step import ProductAnalyticsLaunchDashboardStep
    from datadog_api_client.v2.model.product_analytics_launch_experiment_step import (
        ProductAnalyticsLaunchExperimentStep,
    )
    from datadog_api_client.v2.model.product_analytics_launch_funnel_step import ProductAnalyticsLaunchFunnelStep
    from datadog_api_client.v2.model.product_analytics_launch_tracking_plan import ProductAnalyticsLaunchTrackingPlan


class ProductAnalyticsLaunchSteps(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_dashboard_step import (
            ProductAnalyticsLaunchDashboardStep,
        )
        from datadog_api_client.v2.model.product_analytics_launch_experiment_step import (
            ProductAnalyticsLaunchExperimentStep,
        )
        from datadog_api_client.v2.model.product_analytics_launch_funnel_step import ProductAnalyticsLaunchFunnelStep
        from datadog_api_client.v2.model.product_analytics_launch_tracking_plan import (
            ProductAnalyticsLaunchTrackingPlan,
        )

        return {
            "dashboard": (ProductAnalyticsLaunchDashboardStep,),
            "experiment": (ProductAnalyticsLaunchExperimentStep,),
            "funnel": (ProductAnalyticsLaunchFunnelStep,),
            "tracking_plan": (ProductAnalyticsLaunchTrackingPlan,),
        }

    attribute_map = {
        "dashboard": "dashboard",
        "experiment": "experiment",
        "funnel": "funnel",
        "tracking_plan": "tracking_plan",
    }

    def __init__(
        self_,
        dashboard: Union[ProductAnalyticsLaunchDashboardStep, UnsetType] = unset,
        experiment: Union[ProductAnalyticsLaunchExperimentStep, UnsetType] = unset,
        funnel: Union[ProductAnalyticsLaunchFunnelStep, UnsetType] = unset,
        tracking_plan: Union[ProductAnalyticsLaunchTrackingPlan, UnsetType] = unset,
        **kwargs,
    ):
        """
        Steps of the launch.

        :param dashboard: Dashboard linked to the launch.
        :type dashboard: ProductAnalyticsLaunchDashboardStep, optional

        :param experiment: Experiment linked to the launch. The draft fields are cleared when ``experiment_id`` is set.
        :type experiment: ProductAnalyticsLaunchExperimentStep, optional

        :param funnel: Funnel linked to the launch.
        :type funnel: ProductAnalyticsLaunchFunnelStep, optional

        :param tracking_plan: Tracking plan of a launch, listing the events and properties to instrument.
        :type tracking_plan: ProductAnalyticsLaunchTrackingPlan, optional
        """
        if dashboard is not unset:
            kwargs["dashboard"] = dashboard
        if experiment is not unset:
            kwargs["experiment"] = experiment
        if funnel is not unset:
            kwargs["funnel"] = funnel
        if tracking_plan is not unset:
            kwargs["tracking_plan"] = tracking_plan
        super().__init__(kwargs)
