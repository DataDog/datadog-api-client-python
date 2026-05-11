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
    from datadog_api_client.v2.model.web_integration_account_settings import WebIntegrationAccountSettings


class WebIntegrationAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.web_integration_account_settings import WebIntegrationAccountSettings

        return {
            "name": (str,),
            "settings": (WebIntegrationAccountSettings,),
        }

    attribute_map = {
        "name": "name",
        "settings": "settings",
    }

    def __init__(self_, name: str, settings: Union[WebIntegrationAccountSettings, UnsetType] = unset, **kwargs):
        """
        Attributes object of a web integration account. Secrets are never returned.

        :param name: A human-readable name for the account.
        :type name: str

        :param settings: Integration-specific settings. The shape of this object varies by integration.
        :type settings: WebIntegrationAccountSettings, optional
        """
        if settings is not unset:
            kwargs["settings"] = settings
        super().__init__(kwargs)

        self_.name = name
