# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.action_connection_integration import ActionConnectionIntegration
    from datadog_api_client.v2.model.aws_integration import AWSIntegration
    from datadog_api_client.v2.model.http_integration import HTTPIntegration


class ActionConnectionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.action_connection_integration import ActionConnectionIntegration

        return {
            "integration": (ActionConnectionIntegration,),
            "name": (str,),
        }

    attribute_map = {
        "integration": "integration",
        "name": "name",
    }

    def __init__(
        self_, integration: Union[ActionConnectionIntegration, AWSIntegration, HTTPIntegration], name: str, **kwargs
    ):
        """
        The definition of ``ActionConnectionAttributes`` object.

        :param integration: The definition of ``ActionConnectionIntegration`` object.
        :type integration: ActionConnectionIntegration

        :param name: Name of the connection
        :type name: str
        """
        super().__init__(kwargs)

        self_.integration = integration
        self_.name = name
