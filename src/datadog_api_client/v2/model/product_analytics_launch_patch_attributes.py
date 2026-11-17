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
    from datadog_api_client.v2.model.product_analytics_launch_code_analysis import ProductAnalyticsLaunchCodeAnalysis
    from datadog_api_client.v2.model.product_analytics_launch_kpi import ProductAnalyticsLaunchKPI
    from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
    from datadog_api_client.v2.model.product_analytics_launch_patch_steps import ProductAnalyticsLaunchPatchSteps


class ProductAnalyticsLaunchPatchAttributes(ModelNormal):
    validations = {
        "feature_flag_key": {
            "max_length": 256,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_code_analysis import (
            ProductAnalyticsLaunchCodeAnalysis,
        )
        from datadog_api_client.v2.model.product_analytics_launch_kpi import ProductAnalyticsLaunchKPI
        from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
        from datadog_api_client.v2.model.product_analytics_launch_patch_steps import ProductAnalyticsLaunchPatchSteps

        return {
            "application_id": (str, none_type),
            "code_analysis": (ProductAnalyticsLaunchCodeAnalysis,),
            "context": (str,),
            "description": (str, none_type),
            "feature_flag_id": (str, none_type),
            "feature_flag_key": (str, none_type),
            "kpis": ([ProductAnalyticsLaunchKPI], none_type),
            "name": (str,),
            "phase": (ProductAnalyticsLaunchPhase,),
            "repository_id": (str, none_type),
            "steps": (ProductAnalyticsLaunchPatchSteps,),
        }

    attribute_map = {
        "application_id": "application_id",
        "code_analysis": "code_analysis",
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
        application_id: Union[str, none_type, UnsetType] = unset,
        code_analysis: Union[ProductAnalyticsLaunchCodeAnalysis, UnsetType] = unset,
        context: Union[str, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        feature_flag_id: Union[str, none_type, UnsetType] = unset,
        feature_flag_key: Union[str, none_type, UnsetType] = unset,
        kpis: Union[List[ProductAnalyticsLaunchKPI], none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        phase: Union[ProductAnalyticsLaunchPhase, UnsetType] = unset,
        repository_id: Union[str, none_type, UnsetType] = unset,
        steps: Union[ProductAnalyticsLaunchPatchSteps, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes to update on a launch. Fields that are not set are left unchanged, and ``null`` clears a nullable
        field.
        Setting a non-empty ``feature_flag_id`` clears the stored ``feature_flag_key`` when ``feature_flag_key`` is not set.

        :param application_id: UUID of the RUM application that the launch belongs to.
        :type application_id: str, none_type, optional

        :param code_analysis: Latest inspection of the repository for the tracking plan instrumentation. A new analysis replaces the stored
            one.
            Events and properties that it does not list are not verified.
        :type code_analysis: ProductAnalyticsLaunchCodeAnalysis, optional

        :param context: Context of the feature being launched.
        :type context: str, optional

        :param description: Description of the feature being launched.
        :type description: str, none_type, optional

        :param feature_flag_id: UUID of the Datadog feature flag that gates the launch.
        :type feature_flag_id: str, none_type, optional

        :param feature_flag_key: Key of a feature flag managed outside Datadog. At most 256 characters, with no leading or trailing spaces.
        :type feature_flag_key: str, none_type, optional

        :param kpis: KPIs that the launch is meant to move. Replaces the stored list, and ``null`` clears it.
        :type kpis: [ProductAnalyticsLaunchKPI], none_type, optional

        :param name: Name of the launch.
        :type name: str, optional

        :param phase: Lifecycle phase of a launch. A new launch starts in ``plan`` or ``setup`` , and defaults to ``plan``.
            Allowed changes: ``plan`` to ``setup`` , ``setup`` to ``ready`` , ``ready`` to ``setup`` or ``launched`` , and ``launched`` to
            ``ready``.
        :type phase: ProductAnalyticsLaunchPhase, optional

        :param repository_id: ID of the code repository that implements the feature.
        :type repository_id: str, none_type, optional

        :param steps: Steps to update. Steps that are not set are left unchanged.
            A ``tracking_plan`` replaces the whole stored tracking plan, so include every event and property to keep.
        :type steps: ProductAnalyticsLaunchPatchSteps, optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if code_analysis is not unset:
            kwargs["code_analysis"] = code_analysis
        if context is not unset:
            kwargs["context"] = context
        if description is not unset:
            kwargs["description"] = description
        if feature_flag_id is not unset:
            kwargs["feature_flag_id"] = feature_flag_id
        if feature_flag_key is not unset:
            kwargs["feature_flag_key"] = feature_flag_key
        if kpis is not unset:
            kwargs["kpis"] = kpis
        if name is not unset:
            kwargs["name"] = name
        if phase is not unset:
            kwargs["phase"] = phase
        if repository_id is not unset:
            kwargs["repository_id"] = repository_id
        if steps is not unset:
            kwargs["steps"] = steps
        super().__init__(kwargs)
