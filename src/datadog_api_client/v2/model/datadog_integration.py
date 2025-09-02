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
    from datadog_api_client.v2.model.datadog_credentials import DatadogCredentials
    from datadog_api_client.v2.model.datadog_integration_type import DatadogIntegrationType
    from datadog_api_client.v2.model.datadog_api_key import DatadogAPIKey


class DatadogIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datadog_credentials import DatadogCredentials
        from datadog_api_client.v2.model.datadog_integration_type import DatadogIntegrationType

        return {
            "credentials": (DatadogCredentials,),
            "type": (DatadogIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[DatadogCredentials, DatadogAPIKey], type: DatadogIntegrationType, **kwargs):
        """
        The definition of the ``DatadogIntegration`` object.

        :param credentials: The definition of the ``DatadogCredentials`` object.
        :type credentials: DatadogCredentials

        :param type: The definition of the ``DatadogIntegrationType`` object.
        :type type: DatadogIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
