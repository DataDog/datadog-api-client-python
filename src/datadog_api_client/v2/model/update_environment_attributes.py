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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.environment_subject_authorization_state import EnvironmentSubjectAuthorizationState


class UpdateEnvironmentAttributes(ModelNormal):
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
            "is_production": (bool,),
            "name": (str,),
            "observe_full_evaluation_data": (bool,),
            "queries": ([str],),
            "require_feature_flag_approval": (bool,),
            "subject_authorization_oidc_provider_id": (UUID, none_type),
            "subject_authorization_state": (EnvironmentSubjectAuthorizationState,),
        }

    attribute_map = {
        "is_production": "is_production",
        "name": "name",
        "observe_full_evaluation_data": "observe_full_evaluation_data",
        "queries": "queries",
        "require_feature_flag_approval": "require_feature_flag_approval",
        "subject_authorization_oidc_provider_id": "subject_authorization_oidc_provider_id",
        "subject_authorization_state": "subject_authorization_state",
    }

    def __init__(
        self_,
        is_production: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        observe_full_evaluation_data: Union[bool, UnsetType] = unset,
        queries: Union[List[str], UnsetType] = unset,
        require_feature_flag_approval: Union[bool, UnsetType] = unset,
        subject_authorization_oidc_provider_id: Union[UUID, none_type, UnsetType] = unset,
        subject_authorization_state: Union[EnvironmentSubjectAuthorizationState, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for updating an environment.

        :param is_production: Indicates whether this is a production environment. If omitted, resets to false. Include the existing value to preserve it.
        :type is_production: bool, optional

        :param name: The name of the environment. Required on every request and unique within the organization. Must contain 1 to 200 ASCII characters, start with a letter or digit, and contain only letters, digits, spaces, underscores, hyphens, and periods.
        :type name: str, optional

        :param observe_full_evaluation_data: Controls whether feature flag evaluation events may include original targeting identifiers and full evaluation context. When true, SDKs may include this data. When false, SDKs hash targeting identifiers and omit evaluation context. If omitted, the existing value is preserved.
        :type observe_full_evaluation_data: bool, optional

        :param queries: Required list of at least one exact DD_ENV value associated with this environment. Values cannot be used by another environment in the same organization. Wildcards and search expressions are not supported.
        :type queries: [str], optional

        :param require_feature_flag_approval: Indicates whether feature flag changes require approval in this environment. If omitted, resets to false. Include the existing value to preserve it.
        :type require_feature_flag_approval: bool, optional

        :param subject_authorization_oidc_provider_id: The ID of a Custom OIDC provider, formatted as a nonzero UUID. If omitted, the stored association is preserved. Set to ``null`` to clear the association, which is allowed only when the resulting ``subject_authorization_state`` is ``disabled``. A new non-null ID must be registered in the current organization and site, even when subject authorization is disabled. An unregistered ID returns ``400 Bad Request`` , and an unavailable registry returns ``503 Service Unavailable``. Omitted, cleared, and unchanged IDs skip this check, including when you enable a retained provider. An ID that matches the stored ID in a different format, such as different letter case, is treated as unchanged. Saving does not verify provider eligibility or key publication.
        :type subject_authorization_oidc_provider_id: UUID, none_type, optional

        :param subject_authorization_state: Whether assignment requests for this environment require subject authorization. Allowed values are ``disabled`` and ``enabled``. Enabling requires a provider ID formatted as a nonzero UUID. If omitted on create, defaults to ``disabled``. If omitted on update, the stored state is preserved. ``null`` is not accepted. This setting applies only to the current Datadog site and is not copied to other sites. Before you enable it, configure an eligible Custom OIDC provider in the same organization and site, and verify that the provider's keys are published. Assignment requests fail when the required verification configuration is unavailable.
        :type subject_authorization_state: EnvironmentSubjectAuthorizationState, optional
        """
        if is_production is not unset:
            kwargs["is_production"] = is_production
        if name is not unset:
            kwargs["name"] = name
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
        super().__init__(kwargs)
