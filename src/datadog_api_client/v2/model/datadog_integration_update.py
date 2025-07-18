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
    from datadog_api_client.v2.model.datadog_credentials_update import DatadogCredentialsUpdate
    from datadog_api_client.v2.model.datadog_integration_type import DatadogIntegrationType
    from datadog_api_client.v2.model.datadog_api_key_update import DatadogAPIKeyUpdate


class DatadogIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datadog_credentials_update import DatadogCredentialsUpdate
        from datadog_api_client.v2.model.datadog_integration_type import DatadogIntegrationType

        return {
            "credentials": (DatadogCredentialsUpdate,),
            "type": (DatadogIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: DatadogIntegrationType,
        credentials: Union[DatadogCredentialsUpdate, DatadogAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``DatadogIntegrationUpdate`` object.

        :param credentials: The definition of the ``DatadogCredentialsUpdate`` object.
        :type credentials: DatadogCredentialsUpdate, optional

        :param type: The definition of the ``DatadogIntegrationType`` object.
        :type type: DatadogIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
