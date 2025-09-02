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
    from datadog_api_client.v2.model.asana_credentials_update import AsanaCredentialsUpdate
    from datadog_api_client.v2.model.asana_integration_type import AsanaIntegrationType
    from datadog_api_client.v2.model.asana_access_token_update import AsanaAccessTokenUpdate


class AsanaIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.asana_credentials_update import AsanaCredentialsUpdate
        from datadog_api_client.v2.model.asana_integration_type import AsanaIntegrationType

        return {
            "credentials": (AsanaCredentialsUpdate,),
            "type": (AsanaIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: AsanaIntegrationType,
        credentials: Union[AsanaCredentialsUpdate, AsanaAccessTokenUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``AsanaIntegrationUpdate`` object.

        :param credentials: The definition of the ``AsanaCredentialsUpdate`` object.
        :type credentials: AsanaCredentialsUpdate, optional

        :param type: The definition of the ``AsanaIntegrationType`` object.
        :type type: AsanaIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
