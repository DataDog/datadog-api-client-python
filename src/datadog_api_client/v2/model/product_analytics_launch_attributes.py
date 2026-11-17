# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.product_analytics_launch_kpi import ProductAnalyticsLaunchKPI
    from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
    from datadog_api_client.v2.model.product_analytics_launch_steps import ProductAnalyticsLaunchSteps


class ProductAnalyticsLaunchAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_kpi import ProductAnalyticsLaunchKPI
        from datadog_api_client.v2.model.product_analytics_launch_phase import ProductAnalyticsLaunchPhase
        from datadog_api_client.v2.model.product_analytics_launch_steps import ProductAnalyticsLaunchSteps

        return {
            "application_id": (str, none_type),
            "context": (str, none_type),
            "created_at": (datetime,),
            "created_by": (str,),
            "description": (str, none_type),
            "feature_flag_id": (str, none_type),
            "feature_flag_key": (str, none_type),
            "kpis": ([ProductAnalyticsLaunchKPI], none_type),
            "name": (str,),
            "org_id": (int,),
            "phase": (ProductAnalyticsLaunchPhase,),
            "repository_id": (str,),
            "steps": (ProductAnalyticsLaunchSteps,),
            "updated_at": (datetime, none_type),
            "updated_by": (str, none_type),
        }

    attribute_map = {
        "application_id": "application_id",
        "context": "context",
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "feature_flag_id": "feature_flag_id",
        "feature_flag_key": "feature_flag_key",
        "kpis": "kpis",
        "name": "name",
        "org_id": "org_id",
        "phase": "phase",
        "repository_id": "repository_id",
        "steps": "steps",
        "updated_at": "updated_at",
        "updated_by": "updated_by",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        name: str,
        org_id: int,
        phase: ProductAnalyticsLaunchPhase,
        steps: ProductAnalyticsLaunchSteps,
        application_id: Union[str, none_type, UnsetType] = unset,
        context: Union[str, none_type, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        feature_flag_id: Union[str, none_type, UnsetType] = unset,
        feature_flag_key: Union[str, none_type, UnsetType] = unset,
        kpis: Union[List[ProductAnalyticsLaunchKPI], none_type, UnsetType] = unset,
        repository_id: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, none_type, UnsetType] = unset,
        updated_by: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a launch.

        :param application_id: UUID of the RUM application that the launch belongs to.
        :type application_id: str, none_type, optional

        :param context: Context of the feature being launched.
        :type context: str, none_type, optional

        :param created_at: Time the launch was created.
        :type created_at: datetime

        :param created_by: UUID of the user who created the launch.
        :type created_by: str

        :param description: Description of the feature being launched.
        :type description: str, none_type, optional

        :param feature_flag_id: UUID of the Datadog feature flag that gates the launch.
        :type feature_flag_id: str, none_type, optional

        :param feature_flag_key: Key of a feature flag managed outside Datadog.
        :type feature_flag_key: str, none_type, optional

        :param kpis: KPIs that the launch is meant to move.
        :type kpis: [ProductAnalyticsLaunchKPI], none_type, optional

        :param name: Name of the launch.
        :type name: str

        :param org_id: ID of the organization that owns the launch.
        :type org_id: int

        :param phase: Lifecycle phase of a launch. A new launch starts in ``plan`` or ``setup`` , and defaults to ``plan``.
            Allowed changes: ``plan`` to ``setup`` , ``setup`` to ``ready`` , ``ready`` to ``setup`` or ``launched`` , and ``launched`` to
            ``ready``.
        :type phase: ProductAnalyticsLaunchPhase

        :param repository_id: ID of the code repository that implements the feature.
        :type repository_id: str, optional

        :param steps: Steps of the launch.
        :type steps: ProductAnalyticsLaunchSteps

        :param updated_at: Time the launch was last updated.
        :type updated_at: datetime, none_type, optional

        :param updated_by: UUID of the user who last updated the launch.
        :type updated_by: str, none_type, optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
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
        if repository_id is not unset:
            kwargs["repository_id"] = repository_id
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        if updated_by is not unset:
            kwargs["updated_by"] = updated_by
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.name = name
        self_.org_id = org_id
        self_.phase = phase
        self_.steps = steps
