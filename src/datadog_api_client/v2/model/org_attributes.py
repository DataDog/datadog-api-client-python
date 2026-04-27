# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class OrgAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "description": (str,),
            "disabled": (bool,),
            "modified_at": (datetime,),
            "name": (str,),
            "public_id": (str,),
            "sharing": (str,),
            "url": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "disabled": "disabled",
        "modified_at": "modified_at",
        "name": "name",
        "public_id": "public_id",
        "sharing": "sharing",
        "url": "url",
    }

    def __init__(
        self_,
        created_at: datetime,
        description: str,
        disabled: bool,
        modified_at: datetime,
        name: str,
        public_id: str,
        sharing: str,
        url: str,
        **kwargs,
    ):
        """
        Attributes of an organization.

        :param created_at: The creation timestamp of the organization.
        :type created_at: datetime

        :param description: A description of the organization.
        :type description: str

        :param disabled: Whether the organization is disabled.
        :type disabled: bool

        :param modified_at: The last modification timestamp of the organization.
        :type modified_at: datetime

        :param name: The name of the organization.
        :type name: str

        :param public_id: The public identifier of the organization.
        :type public_id: str

        :param sharing: The sharing setting of the organization.
        :type sharing: str

        :param url: The URL of the organization.
        :type url: str
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.description = description
        self_.disabled = disabled
        self_.modified_at = modified_at
        self_.name = name
        self_.public_id = public_id
        self_.sharing = sharing
        self_.url = url
