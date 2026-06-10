# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
    UUID,
)


class FormPublicationAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "form_id": (UUID,),
            "form_version": (int,),
            "id": (str,),
            "modified_at": (datetime,),
            "org_id": (int,),
            "publish_seq": (int,),
            "user_id": (int,),
            "user_uuid": (UUID,),
        }

    attribute_map = {
        "created_at": "created_at",
        "form_id": "form_id",
        "form_version": "form_version",
        "id": "id",
        "modified_at": "modified_at",
        "org_id": "org_id",
        "publish_seq": "publish_seq",
        "user_id": "user_id",
        "user_uuid": "user_uuid",
    }

    def __init__(
        self_,
        created_at: datetime,
        form_id: UUID,
        form_version: int,
        modified_at: datetime,
        org_id: int,
        publish_seq: int,
        user_id: int,
        user_uuid: UUID,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a form publication.

        :param created_at: The time at which the publication was created.
        :type created_at: datetime

        :param form_id: The ID of the form.
        :type form_id: UUID

        :param form_version: The version number that was published.
        :type form_version: int

        :param id: The ID of the form publication.
        :type id: str, optional

        :param modified_at: The time at which the publication was last modified.
        :type modified_at: datetime

        :param org_id: The ID of the organization that owns this publication.
        :type org_id: int

        :param publish_seq: The sequential publication number for this form.
        :type publish_seq: int

        :param user_id: The ID of the user who created this publication.
        :type user_id: int

        :param user_uuid: The UUID of the user who created this publication.
        :type user_uuid: UUID
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.form_id = form_id
        self_.form_version = form_version
        self_.modified_at = modified_at
        self_.org_id = org_id
        self_.publish_seq = publish_seq
        self_.user_id = user_id
        self_.user_uuid = user_uuid
