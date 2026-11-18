# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
)


class ProductAnalyticsMonitorVariable(ModelNormal):
    def __init__(self_, **kwargs):
        """
        A query variable of the monitor, referenced by name in the ``formula(...)`` of the monitor query.
        Its shape depends on the ``data_source`` , for example ``product_analytics_journey`` for funnels.
        """
        super().__init__(kwargs)
