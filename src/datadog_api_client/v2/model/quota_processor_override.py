# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.field_item import FieldItem
    from datadog_api_client.v2.model.quota_limit import QuotaLimit


class QuotaProcessorOverride(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.field_item import FieldItem
        from datadog_api_client.v2.model.quota_limit import QuotaLimit

        return {
            "fields": ([FieldItem],),
            "limit": (QuotaLimit,),
        }

    attribute_map = {
        "fields": "fields",
        "limit": "limit",
    }

    def __init__(self_, fields: List[FieldItem], limit: QuotaLimit, **kwargs):
        """
        The definition of ``QuotaProcessorOverride`` object.

        :param fields: The ``QuotaProcessorOverride`` ``fields``.
        :type fields: [FieldItem]

        :param limit: Unified definition of ``QuotaLimit`` object.
        :type limit: QuotaLimit
        """
        super().__init__(kwargs)

        self_.fields = fields
        self_.limit = limit
