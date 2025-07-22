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
    from datadog_api_client.v2.model.launch_darkly_credentials_update import LaunchDarklyCredentialsUpdate
    from datadog_api_client.v2.model.launch_darkly_integration_type import LaunchDarklyIntegrationType
    from datadog_api_client.v2.model.launch_darkly_api_key_update import LaunchDarklyAPIKeyUpdate


class LaunchDarklyIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.launch_darkly_credentials_update import LaunchDarklyCredentialsUpdate
        from datadog_api_client.v2.model.launch_darkly_integration_type import LaunchDarklyIntegrationType

        return {
            "credentials": (LaunchDarklyCredentialsUpdate,),
            "type": (LaunchDarklyIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: LaunchDarklyIntegrationType,
        credentials: Union[LaunchDarklyCredentialsUpdate, LaunchDarklyAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``LaunchDarklyIntegrationUpdate`` object.

        :param credentials: The definition of the ``LaunchDarklyCredentialsUpdate`` object.
        :type credentials: LaunchDarklyCredentialsUpdate, optional

        :param type: The definition of the ``LaunchDarklyIntegrationType`` object.
        :type type: LaunchDarklyIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
