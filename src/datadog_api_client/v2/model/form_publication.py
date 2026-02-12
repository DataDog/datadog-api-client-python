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


class FormPublication(ModelNormal):
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
        id: str,
        modified_at: datetime,
        org_id: int,
        user_id: int,
        user_uuid: UUID,
        form_version: Union[int, UnsetType] = unset,
        publish_seq: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Publication information for the form.

        :param created_at: Creation timestamp.
        :type created_at: datetime

        :param form_id: The form identifier.
        :type form_id: UUID

        :param form_version: The version of the form that was published.
        :type form_version: int, optional

        :param id: The unique identifier of the publication.
        :type id: str

        :param modified_at: Last modification timestamp.
        :type modified_at: datetime

        :param org_id: The organization ID.
        :type org_id: int

        :param publish_seq: The publication sequence number.
        :type publish_seq: int, optional

        :param user_id: The ID of the user who published.
        :type user_id: int

        :param user_uuid: The UUID of the user who published.
        :type user_uuid: UUID
        """
        if form_version is not unset:
            kwargs["form_version"] = form_version
        if publish_seq is not unset:
            kwargs["publish_seq"] = publish_seq
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.form_id = form_id
        self_.id = id
        self_.modified_at = modified_at
        self_.org_id = org_id
        self_.user_id = user_id
        self_.user_uuid = user_uuid
