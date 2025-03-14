# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CloudflareAccountUpdateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "api_key": (str,),
            "email": (str,),
            "name": (str,),
            "resources": ([str],),
            "zones": ([str],),
        }

    attribute_map = {
        "api_key": "api_key",
        "email": "email",
        "name": "name",
        "resources": "resources",
        "zones": "zones",
    }

    def __init__(
        self_,
        api_key: str,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        resources: Union[List[str], UnsetType] = unset,
        zones: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes object for updating a Cloudflare account.

        :param api_key: The API key of the Cloudflare account.
        :type api_key: str

        :param email: The email associated with the Cloudflare account. If an API key is provided (and not a token), this field is also required.
        :type email: str, optional

        :param name: The name of the Cloudflare account.
        :type name: str, optional

        :param resources: An allowlist of resources to restrict pulling metrics for including ``'web', 'dns', 'lb' (load balancer), 'worker'``.
        :type resources: [str], optional

        :param zones: An allowlist of zones to restrict pulling metrics for.
        :type zones: [str], optional
        """
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        if resources is not unset:
            kwargs["resources"] = resources
        if zones is not unset:
            kwargs["zones"] = zones
        super().__init__(kwargs)

        self_.api_key = api_key
