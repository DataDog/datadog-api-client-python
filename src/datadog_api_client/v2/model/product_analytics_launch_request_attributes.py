# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_launch_kpi import ProductAnalyticsLaunchKPI
    from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
    from datadog_api_client.v2.model.product_analytics_launch_steps_request import ProductAnalyticsLaunchStepsRequest


class ProductAnalyticsLaunchRequestAttributes(ModelNormal):
    validations = {
        "feature_flag_key": {
            "max_length": 256,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_kpi import ProductAnalyticsLaunchKPI
        from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
        from datadog_api_client.v2.model.product_analytics_launch_steps_request import (
            ProductAnalyticsLaunchStepsRequest,
        )

        return {
            "application_id": (str, none_type),
            "context": (str,),
            "description": (str, none_type),
            "feature_flag_id": (str, none_type),
            "feature_flag_key": (str, none_type),
            "kpis": ([ProductAnalyticsLaunchKPI],),
            "name": (str,),
            "phase": (ProductAnalyticsLaunchPhase,),
            "repository_id": (str,),
            "steps": (ProductAnalyticsLaunchStepsRequest,),
        }

    attribute_map = {
        "application_id": "application_id",
        "context": "context",
        "description": "description",
        "feature_flag_id": "feature_flag_id",
        "feature_flag_key": "feature_flag_key",
        "kpis": "kpis",
        "name": "name",
        "phase": "phase",
        "repository_id": "repository_id",
        "steps": "steps",
    }

    def __init__(
        self_,
        context: str,
        name: str,
        steps: ProductAnalyticsLaunchStepsRequest,
        application_id: Union[str, none_type, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        feature_flag_id: Union[str, none_type, UnsetType] = unset,
        feature_flag_key: Union[str, none_type, UnsetType] = unset,
        kpis: Union[List[ProductAnalyticsLaunchKPI], UnsetType] = unset,
        phase: Union[ProductAnalyticsLaunchPhase, UnsetType] = unset,
        repository_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a launch to create or replace.

        :param application_id: UUID of the RUM application that the launch belongs to.
        :type application_id: str, none_type, optional

        :param context: Context of the feature being launched, used to build the tracking plan.
        :type context: str

        :param description: Description of the feature being launched.
        :type description: str, none_type, optional

        :param feature_flag_id: UUID of the Datadog feature flag that gates the launch. Do not set it together with ``feature_flag_key``.
        :type feature_flag_id: str, none_type, optional

        :param feature_flag_key: Key of a feature flag managed outside Datadog, as evaluated in code. At most 256 characters, with no
            leading or trailing spaces. Do not set it together with ``feature_flag_id``. ``null`` clears it. On replace,
            omitting it keeps the stored key unless ``feature_flag_id`` is set.
        :type feature_flag_key: str, none_type, optional

        :param kpis: KPIs that the launch is meant to move.
        :type kpis: [ProductAnalyticsLaunchKPI], optional

        :param name: Name of the launch.
        :type name: str

        :param phase: Lifecycle phase of a launch. A new launch starts in ``plan`` or ``setup`` , and defaults to ``plan``.
            Allowed changes: ``plan`` to ``setup`` , ``setup`` to ``ready`` , ``ready`` to ``setup`` or ``launched`` , and ``launched`` to
            ``ready``.
        :type phase: ProductAnalyticsLaunchPhase, optional

        :param repository_id: ID of the code repository that implements the feature.
        :type repository_id: str, optional

        :param steps: Steps of the launch. The tracking plan is required.
        :type steps: ProductAnalyticsLaunchStepsRequest
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if description is not unset:
            kwargs["description"] = description
        if feature_flag_id is not unset:
            kwargs["feature_flag_id"] = feature_flag_id
        if feature_flag_key is not unset:
            kwargs["feature_flag_key"] = feature_flag_key
        if kpis is not unset:
            kwargs["kpis"] = kpis
        if phase is not unset:
            kwargs["phase"] = phase
        if repository_id is not unset:
            kwargs["repository_id"] = repository_id
        super().__init__(kwargs)

        self_.context = context
        self_.name = name
        self_.steps = steps
