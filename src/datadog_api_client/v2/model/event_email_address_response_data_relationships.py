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
    from datadog_api_client.v2.model.event_email_address_response_data_relationships_user import (
        EventEmailAddressResponseDataRelationshipsUser,
    )


class EventEmailAddressResponseDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_response_data_relationships_user import (
            EventEmailAddressResponseDataRelationshipsUser,
        )

        return {
            "created_by": (EventEmailAddressResponseDataRelationshipsUser,),
            "revoked_by": (EventEmailAddressResponseDataRelationshipsUser,),
        }

    attribute_map = {
        "created_by": "created_by",
        "revoked_by": "revoked_by",
    }

    def __init__(
        self_,
        created_by: EventEmailAddressResponseDataRelationshipsUser,
        revoked_by: Union[EventEmailAddressResponseDataRelationshipsUser, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param created_by:
        :type created_by: EventEmailAddressResponseDataRelationshipsUser

        :param revoked_by:
        :type revoked_by: EventEmailAddressResponseDataRelationshipsUser, optional
        """
        if revoked_by is not unset:
            kwargs["revoked_by"] = revoked_by
        super().__init__(kwargs)

        self_.created_by = created_by
