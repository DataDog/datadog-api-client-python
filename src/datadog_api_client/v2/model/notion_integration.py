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
    from datadog_api_client.v2.model.notion_credentials import NotionCredentials
    from datadog_api_client.v2.model.notion_integration_type import NotionIntegrationType
    from datadog_api_client.v2.model.notion_api_key import NotionAPIKey


class NotionIntegration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notion_credentials import NotionCredentials
        from datadog_api_client.v2.model.notion_integration_type import NotionIntegrationType

        return {
            "credentials": (NotionCredentials,),
            "type": (NotionIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(self_, credentials: Union[NotionCredentials, NotionAPIKey], type: NotionIntegrationType, **kwargs):
        """
        The definition of the ``NotionIntegration`` object.

        :param credentials: The definition of the ``NotionCredentials`` object.
        :type credentials: NotionCredentials

        :param type: The definition of the ``NotionIntegrationType`` object.
        :type type: NotionIntegrationType
        """
        super().__init__(kwargs)

        self_.credentials = credentials
        self_.type = type
