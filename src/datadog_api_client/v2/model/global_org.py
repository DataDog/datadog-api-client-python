# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class GlobalOrg(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "public_id": (str, none_type),
            "subdomain": (str, none_type),
            "uuid": (UUID,),
        }

    attribute_map = {
        "name": "name",
        "public_id": "public_id",
        "subdomain": "subdomain",
        "uuid": "uuid",
    }

    def __init__(
        self_,
        name: str,
        uuid: UUID,
        public_id: Union[str, none_type, UnsetType] = unset,
        subdomain: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Organization information for a global organization association.

        :param name: The name of the organization.
        :type name: str

        :param public_id: The public identifier of the organization.
        :type public_id: str, none_type, optional

        :param subdomain: The subdomain used to access the organization, if configured.
        :type subdomain: str, none_type, optional

        :param uuid: The UUID of the organization.
        :type uuid: UUID
        """
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if subdomain is not unset:
            kwargs["subdomain"] = subdomain
        super().__init__(kwargs)

        self_.name = name
        self_.uuid = uuid
