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
    from datadog_api_client.v2.model.outcomes_response_data_item import OutcomesResponseDataItem
    from datadog_api_client.v2.model.outcomes_batch_response_meta import OutcomesBatchResponseMeta


class OutcomesBatchResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.outcomes_response_data_item import OutcomesResponseDataItem
        from datadog_api_client.v2.model.outcomes_batch_response_meta import OutcomesBatchResponseMeta

        return {
            "data": ([OutcomesResponseDataItem],),
            "meta": (OutcomesBatchResponseMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[OutcomesResponseDataItem], meta: OutcomesBatchResponseMeta, **kwargs):
        """
        Scorecard outcomes batch response.

        :param data: List of rule outcomes which were affected during the bulk operation.
        :type data: [OutcomesResponseDataItem]

        :param meta: Metadata pertaining to the bulk operation.
        :type meta: OutcomesBatchResponseMeta
        """
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
