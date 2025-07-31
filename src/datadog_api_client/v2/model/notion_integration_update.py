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
    from datadog_api_client.v2.model.notion_credentials_update import NotionCredentialsUpdate
    from datadog_api_client.v2.model.notion_integration_type import NotionIntegrationType
    from datadog_api_client.v2.model.notion_api_key_update import NotionAPIKeyUpdate


class NotionIntegrationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.notion_credentials_update import NotionCredentialsUpdate
        from datadog_api_client.v2.model.notion_integration_type import NotionIntegrationType

        return {
            "credentials": (NotionCredentialsUpdate,),
            "type": (NotionIntegrationType,),
        }

    attribute_map = {
        "credentials": "credentials",
        "type": "type",
    }

    def __init__(
        self_,
        type: NotionIntegrationType,
        credentials: Union[NotionCredentialsUpdate, NotionAPIKeyUpdate, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of the ``NotionIntegrationUpdate`` object.

        :param credentials: The definition of the ``NotionCredentialsUpdate`` object.
        :type credentials: NotionCredentialsUpdate, optional

        :param type: The definition of the ``NotionIntegrationType`` object.
        :type type: NotionIntegrationType
        """
        if credentials is not unset:
            kwargs["credentials"] = credentials
        super().__init__(kwargs)

        self_.type = type
