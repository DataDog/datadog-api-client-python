# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.hamr_org_connection_status import HamrOrgConnectionStatus


class HamrOrgConnectionAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.hamr_org_connection_status import HamrOrgConnectionStatus

        return {
            "hamr_status": (HamrOrgConnectionStatus,),
            "is_primary": (bool,),
            "modified_at": (str,),
            "modified_by": (str,),
            "target_org_datacenter": (str,),
            "target_org_name": (str,),
            "target_org_uuid": (str,),
        }

    attribute_map = {
        "hamr_status": "hamr_status",
        "is_primary": "is_primary",
        "modified_at": "modified_at",
        "modified_by": "modified_by",
        "target_org_datacenter": "target_org_datacenter",
        "target_org_name": "target_org_name",
        "target_org_uuid": "target_org_uuid",
    }

    def __init__(
        self_,
        hamr_status: HamrOrgConnectionStatus,
        is_primary: bool,
        modified_at: str,
        modified_by: str,
        target_org_datacenter: str,
        target_org_name: str,
        target_org_uuid: str,
        **kwargs,
    ):
        """


        :param hamr_status: Status of the HAMR connection:

            * 0: UNSPECIFIED - Connection status not specified
            * 1: ONBOARDING - Initial setup of HAMR connection
            * 2: PASSIVE - Secondary organization in passive standby mode
            * 3: FAILOVER - Liminal status between PASSIVE and ACTIVE
            * 4: ACTIVE - Organization is an active failover
            * 5: RECOVERY - Recovery operation in progress
        :type hamr_status: HamrOrgConnectionStatus

        :param is_primary: Indicates whether this organization is the primary organization in the HAMR relationship.
            If true, this is the primary organization. If false, this is the secondary/backup organization.
        :type is_primary: bool

        :param modified_at: Timestamp of when this HAMR connection was last modified (RFC3339 format).
        :type modified_at: str

        :param modified_by: Username or identifier of the user who last modified this HAMR connection.
        :type modified_by: str

        :param target_org_datacenter: Datacenter location of the target organization (e.g., us1, eu1, us5).
        :type target_org_datacenter: str

        :param target_org_name: Name of the target organization in the HAMR relationship.
        :type target_org_name: str

        :param target_org_uuid: UUID of the target organization in the HAMR relationship.
        :type target_org_uuid: str
        """
        super().__init__(kwargs)

        self_.hamr_status = hamr_status
        self_.is_primary = is_primary
        self_.modified_at = modified_at
        self_.modified_by = modified_by
        self_.target_org_datacenter = target_org_datacenter
        self_.target_org_name = target_org_name
        self_.target_org_uuid = target_org_uuid
