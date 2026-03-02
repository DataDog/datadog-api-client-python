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
    from datadog_api_client.v2.model.llm_obs_experiment_span_meta import LLMObsExperimentSpanMeta


class LLMObsExperimentSpan(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_span_meta import LLMObsExperimentSpanMeta

        return {
            "dataset_id": (str,),
            "duration": (int,),
            "meta": (LLMObsExperimentSpanMeta,),
            "name": (str,),
            "project_id": (str,),
            "span_id": (str,),
            "start_ns": (int,),
            "status": (str,),
            "tags": ([str],),
            "trace_id": (str,),
        }

    attribute_map = {
        "dataset_id": "dataset_id",
        "duration": "duration",
        "meta": "meta",
        "name": "name",
        "project_id": "project_id",
        "span_id": "span_id",
        "start_ns": "start_ns",
        "status": "status",
        "tags": "tags",
        "trace_id": "trace_id",
    }

    def __init__(
        self_,
        dataset_id: str,
        duration: int,
        name: str,
        project_id: str,
        span_id: str,
        start_ns: int,
        status: str,
        trace_id: str,
        meta: Union[LLMObsExperimentSpanMeta, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A span associated with an LLM Observability experiment.

        :param dataset_id: Dataset ID associated with this span.
        :type dataset_id: str

        :param duration: Duration of the span in nanoseconds.
        :type duration: int

        :param meta: Metadata associated with an experiment span.
        :type meta: LLMObsExperimentSpanMeta, optional

        :param name: Name of the span.
        :type name: str

        :param project_id: Project ID associated with this span.
        :type project_id: str

        :param span_id: Unique identifier of the span.
        :type span_id: str

        :param start_ns: Start time of the span in nanoseconds since Unix epoch.
        :type start_ns: int

        :param status: Status of the span.
        :type status: str

        :param tags: List of tags associated with the span.
        :type tags: [str], optional

        :param trace_id: Trace ID for the span.
        :type trace_id: str
        """
        if meta is not unset:
            kwargs["meta"] = meta
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.dataset_id = dataset_id
        self_.duration = duration
        self_.name = name
        self_.project_id = project_id
        self_.span_id = span_id
        self_.start_ns = start_ns
        self_.status = status
        self_.trace_id = trace_id
