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
    from datadog_api_client.v2.model.clickup_credentials import ClickupCredentials
    from datadog_api_client.v2.model.clickup_integration_type import ClickupIntegrationType
    from datadog_api_client.v2.model.clickup_api_key import ClickupAPIKey


class ClickupIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.clickup_credentials import ClickupCredentials
        from datadog_api_client.v2.model.clickup_integration_type import ClickupIntegrationType

        return {
            "credentials": (ClickupCredentials,),
            "type": (ClickupIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[ClickupCredentials, ClickupAPIKey], type: ClickupIntegrationType, **kwargs):
        """
        The definition of the ``ClickupIntegration`` object.

        :param credentials: The definition of the ``ClickupCredentials`` object.
        :type credentials: ClickupCredentials

        :param type: The definition of the ``ClickupIntegrationType`` object.
        :type type: ClickupIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
