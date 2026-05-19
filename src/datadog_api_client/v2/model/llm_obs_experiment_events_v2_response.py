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
    from datadog_api_client.v2.model.llm_obs_experiment_events_v2_data_response import (
        LLMObsExperimentEventsV2DataResponse,
    )
    from datadog_api_client.v2.model.llm_obs_cursor_meta import LLMObsCursorMeta


class LLMObsExperimentEventsV2Response(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_events_v2_data_response import (
            LLMObsExperimentEventsV2DataResponse,
        )
        from datadog_api_client.v2.model.llm_obs_cursor_meta import LLMObsCursorMeta

        return {
            "data": (LLMObsExperimentEventsV2DataResponse,),
            "meta": (LLMObsCursorMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_, data: LLMObsExperimentEventsV2DataResponse, meta: Union[LLMObsCursorMeta, UnsetType] = unset, **kwargs
    ):
        """
        Response for listing experiment events (v2/v3). Returns spans and summary metrics in a single resource.

        :param data: JSON:API data object for an experiment events response.
        :type data: LLMObsExperimentEventsV2DataResponse

        :param meta: Pagination cursor metadata.
        :type meta: LLMObsCursorMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
