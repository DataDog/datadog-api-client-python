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
    from datadog_api_client.v2.model.custom_connection import CustomConnection
    from datadog_api_client.v2.model.deployment_relationship import DeploymentRelationship


class AppRelationship(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_connection import CustomConnection
        from datadog_api_client.v2.model.deployment_relationship import DeploymentRelationship

        return {
            "connections": ([CustomConnection],),
            "deployment": (DeploymentRelationship,),
        }

    attribute_map = {
        "connections": "connections",
        "deployment": "deployment",
    }

    def __init__(
        self_,
        connections: Union[List[CustomConnection], UnsetType] = unset,
        deployment: Union[DeploymentRelationship, UnsetType] = unset,
        **kwargs,
    ):
        """
        The app's publication relationship and custom connections.

        :param connections: Array of custom connections used by the app.
        :type connections: [CustomConnection], optional

        :param deployment: Information pointing to the app's publication status.
        :type deployment: DeploymentRelationship, optional
        """
        if connections is not unset:
            kwargs["connections"] = connections
        if deployment is not unset:
            kwargs["deployment"] = deployment
        super().__init__(kwargs)
