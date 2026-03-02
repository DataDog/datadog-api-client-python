# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.event_email_address_created_by_relationship import (
        EventEmailAddressCreatedByRelationship,
    )
    from datadog_api_client.v2.model.event_email_address_revoked_by_relationship import (
        EventEmailAddressRevokedByRelationship,
    )


class EventEmailAddressRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.event_email_address_created_by_relationship import (
            EventEmailAddressCreatedByRelationship,
        )
        from datadog_api_client.v2.model.event_email_address_revoked_by_relationship import (
            EventEmailAddressRevokedByRelationship,
        )

        return {
            "created_by": (EventEmailAddressCreatedByRelationship,),
            "revoked_by": (EventEmailAddressRevokedByRelationship,),
        }

    attribute_map = {
        "created_by": "created_by",
        "revoked_by": "revoked_by",
    }

    def __init__(
        self_,
        created_by: EventEmailAddressCreatedByRelationship,
        revoked_by: Union[EventEmailAddressRevokedByRelationship, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships associated with an event email address resource.

        :param created_by: Relationship to the user who created the email address.
        :type created_by: EventEmailAddressCreatedByRelationship

        :param revoked_by: Relationship to the user who revoked the email address.
        :type revoked_by: EventEmailAddressRevokedByRelationship, none_type, optional
        """
        if revoked_by is not unset:
            kwargs["revoked_by"] = revoked_by
        super().__init__(kwargs)

        self_.created_by = created_by
