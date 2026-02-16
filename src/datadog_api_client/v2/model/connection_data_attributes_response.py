# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.created_by import CreatedBy
    from datadog_api_client.v2.model.external_secrets_manager import ExternalSecretsManager
    from datadog_api_client.v2.model.private_actions_runner import PrivateActionsRunner
    from datadog_api_client.v2.model.external_secrets_manager_one_of import ExternalSecretsManagerOneOf


class ConnectionDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.created_by import CreatedBy
        from datadog_api_client.v2.model.external_secrets_manager import ExternalSecretsManager
        from datadog_api_client.v2.model.private_actions_runner import PrivateActionsRunner

        return {
            "acting_user_can_resolve": (bool,),
            "created_at": (datetime,),
            "created_by": (CreatedBy,),
            "description": (str,),
            "external_secrets_manager": (ExternalSecretsManager,),
            "integration": (dict,),
            "is_favorite": (bool,),
            "last_updated": (datetime,),
            "name": (str,),
            "private_actions_runner": (PrivateActionsRunner,),
            "runner_id": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "acting_user_can_resolve": "acting_user_can_resolve",
        "created_at": "created_at",
        "created_by": "created_by",
        "description": "description",
        "external_secrets_manager": "external_secrets_manager",
        "integration": "integration",
        "is_favorite": "is_favorite",
        "last_updated": "last_updated",
        "name": "name",
        "private_actions_runner": "private_actions_runner",
        "runner_id": "runner_id",
        "tags": "tags",
    }

    def __init__(
        self_,
        acting_user_can_resolve: bool,
        external_secrets_manager: Union[ExternalSecretsManager, ExternalSecretsManagerOneOf],
        integration: dict,
        is_favorite: bool,
        name: str,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[CreatedBy, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        last_updated: Union[datetime, UnsetType] = unset,
        private_actions_runner: Union[PrivateActionsRunner, UnsetType] = unset,
        runner_id: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an action connection.

        :param acting_user_can_resolve: Indicates if the acting user can resolve the connection.
        :type acting_user_can_resolve: bool

        :param created_at: The creation timestamp of the connection.
        :type created_at: datetime, optional

        :param created_by: Information about the user who created the resource.
        :type created_by: CreatedBy, optional

        :param description: The description of the connection.
        :type description: str, optional

        :param external_secrets_manager: External secrets manager configuration.
        :type external_secrets_manager: ExternalSecretsManager

        :param integration: Integration configuration details.
        :type integration: dict

        :param is_favorite: Indicates if the connection is marked as favorite.
        :type is_favorite: bool

        :param last_updated: The last updated timestamp of the connection.
        :type last_updated: datetime, optional

        :param name: The name of the connection.
        :type name: str

        :param private_actions_runner: Information about the private actions runner.
        :type private_actions_runner: PrivateActionsRunner, optional

        :param runner_id: The ID of the runner associated with the connection.
        :type runner_id: str, optional

        :param tags: Tags associated with the connection.
        :type tags: [str], optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if last_updated is not unset:
            kwargs["last_updated"] = last_updated
        if private_actions_runner is not unset:
            kwargs["private_actions_runner"] = private_actions_runner
        if runner_id is not unset:
            kwargs["runner_id"] = runner_id
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.acting_user_can_resolve = acting_user_can_resolve
        self_.external_secrets_manager = external_secrets_manager
        self_.integration = integration
        self_.is_favorite = is_favorite
        self_.name = name
