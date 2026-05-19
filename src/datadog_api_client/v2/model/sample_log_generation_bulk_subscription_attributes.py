# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sample_log_generation_duration import SampleLogGenerationDuration


class SampleLogGenerationBulkSubscriptionAttributes(ModelNormal):
    validations = {
        "content_pack_ids": {
            "max_items": 5,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sample_log_generation_duration import SampleLogGenerationDuration

        return {
            "content_pack_ids": ([str],),
            "duration": (SampleLogGenerationDuration,),
        }

    attribute_map = {
        "content_pack_ids": "content_pack_ids",
        "duration": "duration",
    }

    def __init__(
        self_, content_pack_ids: List[str], duration: Union[SampleLogGenerationDuration, UnsetType] = unset, **kwargs
    ):
        """
        The attributes for creating sample log generation subscriptions for multiple content packs.

        :param content_pack_ids: The identifiers of the Cloud SIEM content packs to subscribe to. At most five content packs can be requested in a single call.
        :type content_pack_ids: [str]

        :param duration: How long the subscription should remain active before expiring.
        :type duration: SampleLogGenerationDuration, optional
        """
        if duration is not unset:
            kwargs["duration"] = duration
        super().__init__(kwargs)

        self_.content_pack_ids = content_pack_ids
