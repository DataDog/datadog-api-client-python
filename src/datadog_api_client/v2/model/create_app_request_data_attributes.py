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
    from datadog_api_client.v2.model.component_grid import ComponentGrid
    from datadog_api_client.v2.model.query import Query
    from datadog_api_client.v2.model.action_query import ActionQuery
    from datadog_api_client.v2.model.data_transform import DataTransform
    from datadog_api_client.v2.model.state_variable import StateVariable


class CreateAppRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.component_grid import ComponentGrid
        from datadog_api_client.v2.model.query import Query

        return {
            "components": ([ComponentGrid],),
            "description": (str,),
            "name": (str,),
            "queries": ([Query],),
            "root_instance_name": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "components": "components",
        "description": "description",
        "name": "name",
        "queries": "queries",
        "root_instance_name": "rootInstanceName",
        "tags": "tags",
    }

    def __init__(
        self_,
        components: Union[List[ComponentGrid], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        queries: Union[List[Union[Query, ActionQuery, DataTransform, StateVariable]], UnsetType] = unset,
        root_instance_name: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        App definition attributes such as name, description, and components.

        :param components: The UI components that make up the app.
        :type components: [ComponentGrid], optional

        :param description: A human-readable description for the app.
        :type description: str, optional

        :param name: The name of the app.
        :type name: str, optional

        :param queries: An array of queries, such as external actions and state variables, that the app uses.
        :type queries: [Query], optional

        :param root_instance_name: The name of the root component of the app. This must be a ``grid`` component that contains all other components.
        :type root_instance_name: str, optional

        :param tags: A list of tags for the app, which can be used to filter apps.
        :type tags: [str], optional
        """
        if components is not unset:
            kwargs["components"] = components
        if description is not unset:
            kwargs["description"] = description
        if name is not unset:
            kwargs["name"] = name
        if queries is not unset:
            kwargs["queries"] = queries
        if root_instance_name is not unset:
            kwargs["root_instance_name"] = root_instance_name
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
