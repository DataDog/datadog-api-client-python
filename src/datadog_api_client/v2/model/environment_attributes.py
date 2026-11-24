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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.environment_subject_authorization_state import EnvironmentSubjectAuthorizationState


class EnvironmentAttributes(ModelNormal):
    validations = {
        "queries": {
            "min_items": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.environment_subject_authorization_state import (
            EnvironmentSubjectAuthorizationState,
        )

        return {
            "created_at": (datetime,),
            "is_production": (bool,),
            "name": (str,),
            "observe_full_evaluation_data": (bool,),
            "queries": ([str],),
            "require_feature_flag_approval": (bool,),
            "subject_authorization_oidc_provider_id": (UUID, none_type),
            "subject_authorization_state": (EnvironmentSubjectAuthorizationState,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "is_production": "is_production",
        "name": "name",
        "observe_full_evaluation_data": "observe_full_evaluation_data",
        "queries": "queries",
        "require_feature_flag_approval": "require_feature_flag_approval",
        "subject_authorization_oidc_provider_id": "subject_authorization_oidc_provider_id",
        "subject_authorization_state": "subject_authorization_state",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        name: str,
        created_at: Union[datetime, UnsetType] = unset,
        is_production: Union[bool, UnsetType] = unset,
        observe_full_evaluation_data: Union[bool, UnsetType] = unset,
        queries: Union[List[str], UnsetType] = unset,
        require_feature_flag_approval: Union[bool, UnsetType] = unset,
        subject_authorization_oidc_provider_id: Union[UUID, none_type, UnsetType] = unset,
        subject_authorization_state: Union[EnvironmentSubjectAuthorizationState, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an environment.

        :param created_at: The timestamp when the environment was created.
        :type created_at: datetime, optional

        :param is_production: Indicates whether this is a production environment.
        :type is_production: bool, optional

        :param name: The name of the environment.
        :type name: str

        :param observe_full_evaluation_data: Indicates whether feature flag evaluation events include original targeting identifiers and full evaluation context.
        :type observe_full_evaluation_data: bool, optional

        :param queries: List of queries to define the environment scope.
        :type queries: [str], optional

        :param require_feature_flag_approval: Indicates whether feature flag changes require approval in this environment.
        :type require_feature_flag_approval: bool, optional

        :param subject_authorization_oidc_provider_id: The associated Custom OIDC provider ID, or ``null`` when no provider is associated. Disabled environments may retain a provider association.
        :type subject_authorization_oidc_provider_id: UUID, none_type, optional

        :param subject_authorization_state: Whether assignment requests for this environment require subject authorization. Allowed values are ``disabled`` and ``enabled``. Enabling requires a provider ID formatted as a nonzero UUID. If omitted on create, defaults to ``disabled``. If omitted on update, the stored state is preserved. ``null`` is not accepted. This setting applies only to the current Datadog site and is not copied to other sites. Before you enable it, configure an eligible Custom OIDC provider in the same organization and site, and verify that the provider's keys are published. Assignment requests fail when the required verification configuration is unavailable.
        :type subject_authorization_state: EnvironmentSubjectAuthorizationState, optional

        :param updated_at: The timestamp when the environment was last updated.
        :type updated_at: datetime, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if is_production is not unset:
            kwargs["is_production"] = is_production
        if observe_full_evaluation_data is not unset:
            kwargs["observe_full_evaluation_data"] = observe_full_evaluation_data
        if queries is not unset:
            kwargs["queries"] = queries
        if require_feature_flag_approval is not unset:
            kwargs["require_feature_flag_approval"] = require_feature_flag_approval
        if subject_authorization_oidc_provider_id is not unset:
            kwargs["subject_authorization_oidc_provider_id"] = subject_authorization_oidc_provider_id
        if subject_authorization_state is not unset:
            kwargs["subject_authorization_state"] = subject_authorization_state
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.name = name
