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
    from datadog_api_client.v2.model.update_outcomes_async_request_item import UpdateOutcomesAsyncRequestItem


class UpdateOutcomesAsyncAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_outcomes_async_request_item import UpdateOutcomesAsyncRequestItem

        return {
            "results": ([UpdateOutcomesAsyncRequestItem],),
        }

    attribute_map = {
        "results": "results",
    }

    def __init__(self_, results: Union[List[UpdateOutcomesAsyncRequestItem], UnsetType] = unset, **kwargs):
        """
        The JSON:API attributes for a batched set of scorecard outcomes.

        :param results: Set of scorecard outcomes to update asynchronously.
        :type results: [UpdateOutcomesAsyncRequestItem], optional
        """
        if results is not unset:
            kwargs["results"] = results
        super().__init__(kwargs)
