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
    from datadog_api_client.v2.model.fastly_credentials_update import FastlyCredentialsUpdate
    from datadog_api_client.v2.model.fastly_integration_type import FastlyIntegrationType
    from datadog_api_client.v2.model.fastly_api_key_update import FastlyAPIKeyUpdate


class FastlyIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.fastly_credentials_update import FastlyCredentialsUpdate
        from datadog_api_client.v2.model.fastly_integration_type import FastlyIntegrationType

        return {
            "credentials": (FastlyCredentialsUpdate,),
            "type": (FastlyIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: FastlyIntegrationType,
        credentials: Union[FastlyCredentialsUpdate, FastlyAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``FastlyIntegrationUpdate`` object.

        :param credentials: The definition of the ``FastlyCredentialsUpdate`` object.
        :type credentials: FastlyCredentialsUpdate, optional

        :param type: The definition of the ``FastlyIntegrationType`` object.
        :type type: FastlyIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
