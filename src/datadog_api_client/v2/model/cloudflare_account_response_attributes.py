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


class CloudflareAccountResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "name": (str,),
            "resources": ([str],),
            "zones": ([str],),
        }

    attribute_map = {
        "email": "email",
        "name": "name",
        "resources": "resources",
        "zones": "zones",
    }

    def __init__(
        self_,
        name: str,
        email: Union[str, UnsetType] = unset,
        resources: Union[List[str], UnsetType] = unset,
        zones: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes object of a Cloudflare account.

        :param email: The email associated with the Cloudflare account.
        :type email: str, optional

        :param name: The name of the Cloudflare account.
        :type name: str

        :param resources: An allowlist of resources to restrict pulling metrics for.
        :type resources: [str], optional

        :param zones: An allowlist of zones to restrict pulling metrics for.
        :type zones: [str], optional
        """
        if email is not unset:
            kwargs["email"] = email
        if resources is not unset:
            kwargs["resources"] = resources
        if zones is not unset:
            kwargs["zones"] = zones
        super().__init__(kwargs)

        self_.name = name
