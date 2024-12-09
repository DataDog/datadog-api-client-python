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
    from datadog_api_client.v2.model.input_schema import InputSchema
    from datadog_api_client.v2.model.script import Script


class CreateAppRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.component_grid import ComponentGrid
        from datadog_api_client.v2.model.query import Query
        from datadog_api_client.v2.model.input_schema import InputSchema
        from datadog_api_client.v2.model.script import Script

        return {
            "components": ([ComponentGrid],),
            "description": (str,),
            "embedded_queries": ([Query],),
            "input_schema": (InputSchema,),
            "name": (str,),
            "root_instance_name": (str,),
            "scripts": ([Script],),
            "tags": ([str],),
        }

    attribute_map = {
        "components": "components",
        "description": "description",
        "embedded_queries": "embeddedQueries",
        "input_schema": "inputSchema",
        "name": "name",
        "root_instance_name": "rootInstanceName",
        "scripts": "scripts",
        "tags": "tags",
    }

    def __init__(
        self_,
        components: Union[List[ComponentGrid], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        embedded_queries: Union[List[Query], UnsetType] = unset,
        input_schema: Union[InputSchema, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        root_instance_name: Union[str, UnsetType] = unset,
        scripts: Union[List[Script], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateAppRequestDataAttributes`` object.

        :param components: The ``attributes`` ``components``.
        :type components: [ComponentGrid], optional

        :param description: The ``attributes`` ``description``.
        :type description: str, optional

        :param embedded_queries: The ``attributes`` ``embeddedQueries``.
        :type embedded_queries: [Query], optional

        :param input_schema: The definition of ``InputSchema`` object.
        :type input_schema: InputSchema, optional

        :param name: The ``attributes`` ``name``.
        :type name: str, optional

        :param root_instance_name: The ``attributes`` ``rootInstanceName``.
        :type root_instance_name: str, optional

        :param scripts: The ``attributes`` ``scripts``.
        :type scripts: [Script], optional

        :param tags: The ``attributes`` ``tags``.
        :type tags: [str], optional
        """
        if components is not unset:
            kwargs["components"] = components
        if description is not unset:
            kwargs["description"] = description
        if embedded_queries is not unset:
            kwargs["embedded_queries"] = embedded_queries
        if input_schema is not unset:
            kwargs["input_schema"] = input_schema
        if name is not unset:
            kwargs["name"] = name
        if root_instance_name is not unset:
            kwargs["root_instance_name"] = root_instance_name
        if scripts is not unset:
            kwargs["scripts"] = scripts
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
