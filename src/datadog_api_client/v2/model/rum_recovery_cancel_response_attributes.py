# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_recovery_discovery_status import RumRecoveryDiscoveryStatus


class RumRecoveryCancelResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_discovery_status import RumRecoveryDiscoveryStatus

        return {
            "cancelled_at": (datetime,),
            "cancelled_by": (str,),
            "discovery_status": (RumRecoveryDiscoveryStatus,),
        }

    attribute_map = {
        "cancelled_at": "cancelled_at",
        "cancelled_by": "cancelled_by",
        "discovery_status": "discovery_status",
    }

    def __init__(
        self_, cancelled_at: datetime, cancelled_by: str, discovery_status: RumRecoveryDiscoveryStatus, **kwargs
    ):
        """
        Batch cancellation acknowledgment.

        :param cancelled_at: Cancellation time.
        :type cancelled_at: datetime

        :param cancelled_by: Handle of the user who canceled the batch.
        :type cancelled_by: str

        :param discovery_status: Batch discovery state. QUEUED indicates that the request is waiting for processing capacity.
        :type discovery_status: RumRecoveryDiscoveryStatus
        """
        super().__init__(kwargs)

        self_.cancelled_at = cancelled_at
        self_.cancelled_by = cancelled_by
        self_.discovery_status = discovery_status
