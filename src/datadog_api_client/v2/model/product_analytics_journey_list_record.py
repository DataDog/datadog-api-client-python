# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class ProductAnalyticsJourneyListRecord(ModelNormal):
    def __init__(self_, **kwargs):
        """
        A single row. Keys are the returned column names: the identity join key, ``timestamp`` ,
        each entry of ``entity_columns`` , and any computed columns. A value is null when the
        column has no value for that row.
        """
        super().__init__(kwargs)
