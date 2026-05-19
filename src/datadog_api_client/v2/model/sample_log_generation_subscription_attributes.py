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
    from datadog_api_client.v2.model.sample_log_generation_subscription_status import (
        SampleLogGenerationSubscriptionStatus,
    )


class SampleLogGenerationSubscriptionAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_subscription_status import (
            SampleLogGenerationSubscriptionStatus,
        )

        return {
            "content_pack_id": (str,),
            "created_at": (datetime,),
            "expires_at": (datetime,),
            "is_active": (bool,),
            "status": (SampleLogGenerationSubscriptionStatus,),
        }

    attribute_map = {
        "content_pack_id": "content_pack_id",
        "created_at": "created_at",
        "expires_at": "expires_at",
        "is_active": "is_active",
        "status": "status",
    }

    def __init__(
        self_,
        content_pack_id: str,
        created_at: datetime,
        expires_at: datetime,
        is_active: bool,
        status: SampleLogGenerationSubscriptionStatus,
        **kwargs,
    ):
        """
        The attributes describing a sample log generation subscription.

        :param content_pack_id: The identifier of the Cloud SIEM content pack the subscription targets.
        :type content_pack_id: str

        :param created_at: The time at which the subscription was created.
        :type created_at: datetime

        :param expires_at: The time at which the subscription expires and stops generating logs.
        :type expires_at: datetime

        :param is_active: Whether the subscription is currently active and generating logs.
        :type is_active: bool

        :param status: The status of the subscription.
        :type status: SampleLogGenerationSubscriptionStatus
        """
        super().__init__(kwargs)

        self_.content_pack_id = content_pack_id
        self_.created_at = created_at
        self_.expires_at = expires_at
        self_.is_active = is_active
        self_.status = status
