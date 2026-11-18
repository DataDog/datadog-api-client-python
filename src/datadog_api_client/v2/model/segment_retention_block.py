# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class SegmentRetentionBlock(ModelNormal):
    def __init__(self_, **kwargs):
        """
        Selects users from a retention query. It has the same fields as a Product Analytics retention query, plus a
        ``name``.
        """
        super().__init__(kwargs)
