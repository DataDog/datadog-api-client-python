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
    from datadog_api_client.v2.model.connection_group import ConnectionGroup
    from datadog_api_client.v2.model.connection import Connection
    from datadog_api_client.v2.model.connection_env_env import ConnectionEnvEnv


class ConnectionEnv(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.connection_group import ConnectionGroup
        from datadog_api_client.v2.model.connection import Connection
        from datadog_api_client.v2.model.connection_env_env import ConnectionEnvEnv

        return {
            "connection_groups": ([ConnectionGroup],),
            "connections": ([Connection],),
            "env": (ConnectionEnvEnv,),
        }

    attribute_map = {
        "connection_groups": "connectionGroups",
        "connections": "connections",
        "env": "env",
    }

    def __init__(
        self_,
        env: ConnectionEnvEnv,
        connection_groups: Union[List[ConnectionGroup], UnsetType] = unset,
        connections: Union[List[Connection], UnsetType] = unset,
        **kwargs,
    ):
        """
        A list of connections or connection groups used in the workflow.

        :param connection_groups: The ``ConnectionEnv`` ``connectionGroups``.
        :type connection_groups: [ConnectionGroup], optional

        :param connections: The ``ConnectionEnv`` ``connections``.
        :type connections: [Connection], optional

        :param env: The definition of ``ConnectionEnvEnv`` object.
        :type env: ConnectionEnvEnv
        """
        if connection_groups is not unset:
            kwargs["connection_groups"] = connection_groups
        if connections is not unset:
            kwargs["connections"] = connections
        super().__init__(kwargs)

        self_.env = env
