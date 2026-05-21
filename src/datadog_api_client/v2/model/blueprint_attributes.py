# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.app_definition_type import AppDefinitionType
    from datadog_api_client.v2.model.blueprint_native_action import BlueprintNativeAction


class BlueprintAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.app_definition_type import AppDefinitionType
        from datadog_api_client.v2.model.blueprint_native_action import BlueprintNativeAction

        return {
            "created_at": (datetime,),
            "definition": (AppDefinitionType,),
            "description": (str,),
            "embedded_datastore_blueprints": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "embedded_native_actions": ([BlueprintNativeAction],),
            "embedded_workflow_blueprints": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "integration_id": (str,),
            "mocked_outputs": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "name": (str,),
            "slug": (str,),
            "tags": ([str],),
            "tile_background": (str,),
            "tile_icon_action_fqn": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "created_at": "created_at",
        "definition": "definition",
        "description": "description",
        "embedded_datastore_blueprints": "embedded_datastore_blueprints",
        "embedded_native_actions": "embedded_native_actions",
        "embedded_workflow_blueprints": "embedded_workflow_blueprints",
        "integration_id": "integration_id",
        "mocked_outputs": "mocked_outputs",
        "name": "name",
        "slug": "slug",
        "tags": "tags",
        "tile_background": "tile_background",
        "tile_icon_action_fqn": "tile_icon_action_fqn",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: datetime,
        definition: AppDefinitionType,
        description: str,
        name: str,
        slug: str,
        updated_at: datetime,
        embedded_datastore_blueprints: Union[Dict[str, Any], UnsetType] = unset,
        embedded_native_actions: Union[List[BlueprintNativeAction], UnsetType] = unset,
        embedded_workflow_blueprints: Union[Dict[str, Any], UnsetType] = unset,
        integration_id: Union[str, UnsetType] = unset,
        mocked_outputs: Union[Dict[str, Any], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        tile_background: Union[str, UnsetType] = unset,
        tile_icon_action_fqn: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a blueprint resource.

        :param created_at: The timestamp when the blueprint was created.
        :type created_at: datetime

        :param definition: The app definition type.
        :type definition: AppDefinitionType

        :param description: A description of what the blueprint does.
        :type description: str

        :param embedded_datastore_blueprints: Embedded datastore blueprints.
        :type embedded_datastore_blueprints: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param embedded_native_actions: Embedded native actions.
        :type embedded_native_actions: [BlueprintNativeAction], optional

        :param embedded_workflow_blueprints: Embedded workflow blueprints.
        :type embedded_workflow_blueprints: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param integration_id: The integration ID associated with the blueprint.
        :type integration_id: str, optional

        :param mocked_outputs: Mocked outputs for testing the blueprint.
        :type mocked_outputs: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: The human-readable name of the blueprint.
        :type name: str

        :param slug: The unique slug identifier of the blueprint.
        :type slug: str

        :param tags: Tags associated with the blueprint.
        :type tags: [str], optional

        :param tile_background: The background style of the blueprint tile.
        :type tile_background: str, optional

        :param tile_icon_action_fqn: The fully qualified name of the action used as the tile icon.
        :type tile_icon_action_fqn: str, optional

        :param updated_at: The timestamp when the blueprint was last updated.
        :type updated_at: datetime
        """
        if embedded_datastore_blueprints is not unset:
            kwargs["embedded_datastore_blueprints"] = embedded_datastore_blueprints
        if embedded_native_actions is not unset:
            kwargs["embedded_native_actions"] = embedded_native_actions
        if embedded_workflow_blueprints is not unset:
            kwargs["embedded_workflow_blueprints"] = embedded_workflow_blueprints
        if integration_id is not unset:
            kwargs["integration_id"] = integration_id
        if mocked_outputs is not unset:
            kwargs["mocked_outputs"] = mocked_outputs
        if tags is not unset:
            kwargs["tags"] = tags
        if tile_background is not unset:
            kwargs["tile_background"] = tile_background
        if tile_icon_action_fqn is not unset:
            kwargs["tile_icon_action_fqn"] = tile_icon_action_fqn
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.definition = definition
        self_.description = description
        self_.name = name
        self_.slug = slug
        self_.updated_at = updated_at
