# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.action_connection_integration_update import ActionConnectionIntegrationUpdate
    from datadog_api_client.v2.model.aws_integration_update import AWSIntegrationUpdate
    from datadog_api_client.v2.model.http_integration_update import HTTPIntegrationUpdate


class ActionConnectionAttributesUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_integration_update import ActionConnectionIntegrationUpdate

        return {
            "integration": (ActionConnectionIntegrationUpdate,),
            "name": (str,),
        }

    attribute_map = {
        "integration": "integration",
        "name": "name",
    }

    def __init__(
        self_,
        integration: Union[
            ActionConnectionIntegrationUpdate, AWSIntegrationUpdate, HTTPIntegrationUpdate, UnsetType
        ] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``ActionConnectionAttributesUpdate`` object.

        :param integration: The definition of ``ActionConnectionIntegrationUpdate`` object.
        :type integration: ActionConnectionIntegrationUpdate, optional

        :param name: Name of the connection
        :type name: str, optional
        """
        if integration is not unset:
            kwargs["integration"] = integration
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
