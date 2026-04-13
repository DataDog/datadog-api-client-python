# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class OrgGroupPolicyOverrideAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "created_at": (datetime,),
            "modified_at": (datetime,),
            "org_site": (str,),
            "org_uuid": (UUID,),
        }

    attribute_map = {
        "content": "content",
        "created_at": "created_at",
        "modified_at": "modified_at",
        "org_site": "org_site",
        "org_uuid": "org_uuid",
    }

    def __init__(
        self_,
        created_at: datetime,
        modified_at: datetime,
        org_site: str,
        org_uuid: UUID,
        content: Union[Dict[str, Any], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an org group policy override.

        :param content: The override content as key-value pairs.
        :type content: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param created_at: Timestamp when the override was created.
        :type created_at: datetime

        :param modified_at: Timestamp when the override was last modified.
        :type modified_at: datetime

        :param org_site: The site of the organization that has the override.
        :type org_site: str

        :param org_uuid: The UUID of the organization that has the override.
        :type org_uuid: UUID
        """
        if content is not unset:
            kwargs["content"] = content
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.modified_at = modified_at
        self_.org_site = org_site
        self_.org_uuid = org_uuid
