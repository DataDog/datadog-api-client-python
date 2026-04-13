# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    UUID,
)


class OrgGroupMembershipAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "org_name": (str,),
            "org_site": (str,),
            "org_uuid": (UUID,),
        }

    attribute_map = {
        "created_at": "created_at",
        "modified_at": "modified_at",
        "org_name": "org_name",
        "org_site": "org_site",
        "org_uuid": "org_uuid",
    }

    def __init__(
        self_, created_at: datetime, modified_at: datetime, org_name: str, org_site: str, org_uuid: UUID, **kwargs
    ):
        """
        Attributes of an org group membership.

        :param created_at: Timestamp when the membership was created.
        :type created_at: datetime

        :param modified_at: Timestamp when the membership was last modified.
        :type modified_at: datetime

        :param org_name: The name of the member organization.
        :type org_name: str

        :param org_site: The site of the member organization.
        :type org_site: str

        :param org_uuid: The UUID of the member organization.
        :type org_uuid: UUID
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.modified_at = modified_at
        self_.org_name = org_name
        self_.org_site = org_site
        self_.org_uuid = org_uuid
