# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.attachment_data_relationships_last_modified_by_user import (
        AttachmentDataRelationshipsLastModifiedByUser,
    )


class AttachmentDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.attachment_data_relationships_last_modified_by_user import (
            AttachmentDataRelationshipsLastModifiedByUser,
        )

        return {
            "last_modified_by_user": (AttachmentDataRelationshipsLastModifiedByUser,),
        }

    attribute_map = {
        "last_modified_by_user": "last_modified_by_user",
    }

    def __init__(
        self_, last_modified_by_user: Union[AttachmentDataRelationshipsLastModifiedByUser, UnsetType] = unset, **kwargs
    ):
        """


        :param last_modified_by_user:
        :type last_modified_by_user: AttachmentDataRelationshipsLastModifiedByUser, optional
        """
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        super().__init__(kwargs)
