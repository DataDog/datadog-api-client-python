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
    from datadog_api_client.v2.model.outcomes_batch_request_item import OutcomesBatchRequestItem


class OutcomesBatchAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.outcomes_batch_request_item import OutcomesBatchRequestItem

        return {
            "results": ([OutcomesBatchRequestItem],),
        }

    attribute_map = {
        "results": "results",
    }

    def __init__(self_, results: Union[List[OutcomesBatchRequestItem], UnsetType] = unset, **kwargs):
        """
        The JSON:API attributes for a batched set of scorecard outcomes.

        :param results: Set of scorecard outcomes to update.
        :type results: [OutcomesBatchRequestItem], optional
        """
        if results is not unset:
            kwargs["results"] = results
        super().__init__(kwargs)
