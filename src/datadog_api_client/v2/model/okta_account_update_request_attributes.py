# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class OktaAccountUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_key": (str,),
            "auth_method": (str,),
            "client_id": (str,),
            "client_secret": (str,),
            "domain": (str,),
        }

    attribute_map = {
        "api_key": "api_key",
        "auth_method": "auth_method",
        "client_id": "client_id",
        "client_secret": "client_secret",
        "domain": "domain",
    }

    def __init__(
        self_,
        auth_method: str,
        domain: str,
        api_key: Union[str, UnsetType] = unset,
        client_id: Union[str, UnsetType] = unset,
        client_secret: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes object for updating an Okta account.

        :param api_key: The API key of the Okta account.
        :type api_key: str, optional

        :param auth_method: The authorization method for an Okta account.
        :type auth_method: str

        :param client_id: The Client ID of an Okta app integration.
        :type client_id: str, optional

        :param client_secret: The client secret of an Okta app integration.
        :type client_secret: str, optional

        :param domain: The domain associated with an Okta account.
        :type domain: str
        """
        if api_key is not unset:
            kwargs["api_key"] = api_key
        if client_id is not unset:
            kwargs["client_id"] = client_id
        if client_secret is not unset:
            kwargs["client_secret"] = client_secret
        super().__init__(kwargs)

        self_.auth_method = auth_method
        self_.domain = domain
