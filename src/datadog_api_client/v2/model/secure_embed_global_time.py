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
    from datadog_api_client.v2.model.secure_embed_global_time_live_span import SecureEmbedGlobalTimeLiveSpan


class SecureEmbedGlobalTime(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.secure_embed_global_time_live_span import SecureEmbedGlobalTimeLiveSpan

        return {
            "live_span": (SecureEmbedGlobalTimeLiveSpan,),
        }

    attribute_map = {
        "live_span": "live_span",
    }

    def __init__(self_, live_span: Union[SecureEmbedGlobalTimeLiveSpan, UnsetType] = unset, **kwargs):
        """
        Default time range configuration for the secure embed.

        :param live_span: Dashboard global time live_span selection.
        :type live_span: SecureEmbedGlobalTimeLiveSpan, optional
        """
        if live_span is not unset:
            kwargs["live_span"] = live_span
        super().__init__(kwargs)
