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


class OrgGroupAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "name": (str,),
            "owner_org_site": (str,),
            "owner_org_uuid": (UUID,),
        }

    attribute_map = {
        "created_at": "created_at",
        "modified_at": "modified_at",
        "name": "name",
        "owner_org_site": "owner_org_site",
        "owner_org_uuid": "owner_org_uuid",
    }

    def __init__(
        self_,
        created_at: datetime,
        modified_at: datetime,
        name: str,
        owner_org_site: str,
        owner_org_uuid: UUID,
        **kwargs,
    ):
        """
        Attributes of an org group.

        :param created_at: Timestamp when the org group was created.
        :type created_at: datetime

        :param modified_at: Timestamp when the org group was last modified.
        :type modified_at: datetime

        :param name: The name of the org group.
        :type name: str

        :param owner_org_site: The site of the organization that owns this org group.
        :type owner_org_site: str

        :param owner_org_uuid: The UUID of the organization that owns this org group.
        :type owner_org_uuid: UUID
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.modified_at = modified_at
        self_.name = name
        self_.owner_org_site = owner_org_site
        self_.owner_org_uuid = owner_org_uuid
