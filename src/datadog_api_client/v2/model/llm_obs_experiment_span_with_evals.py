# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_experiment_eval_metric_event import LLMObsExperimentEvalMetricEvent
    from datadog_api_client.v2.model.llm_obs_experiment_span_meta import LLMObsExperimentSpanMeta
    from datadog_api_client.v2.model.llm_obs_experiment_span_status import LLMObsExperimentSpanStatus


class LLMObsExperimentSpanWithEvals(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_experiment_eval_metric_event import LLMObsExperimentEvalMetricEvent
        from datadog_api_client.v2.model.llm_obs_experiment_span_meta import LLMObsExperimentSpanMeta
        from datadog_api_client.v2.model.llm_obs_experiment_span_status import LLMObsExperimentSpanStatus

        return {
            "dataset_record_id": (str, none_type),
            "duration": (float,),
            "eval_metrics": ([LLMObsExperimentEvalMetricEvent],),
            "id": (str,),
            "meta": (LLMObsExperimentSpanMeta,),
            "metrics": ({str: (float,)},),
            "name": (str,),
            "parent_id": (str,),
            "span_id": (str,),
            "start_ns": (int,),
            "status": (LLMObsExperimentSpanStatus,),
            "tags": ([str],),
            "trace_id": (str,),
        }

    attribute_map = {
        "dataset_record_id": "dataset_record_id",
        "duration": "duration",
        "eval_metrics": "eval_metrics",
        "id": "id",
        "meta": "meta",
        "metrics": "metrics",
        "name": "name",
        "parent_id": "parent_id",
        "span_id": "span_id",
        "start_ns": "start_ns",
        "status": "status",
        "tags": "tags",
        "trace_id": "trace_id",
    }

    def __init__(
        self_,
        dataset_record_id: Union[str, none_type, UnsetType] = unset,
        duration: Union[float, UnsetType] = unset,
        eval_metrics: Union[List[LLMObsExperimentEvalMetricEvent], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        meta: Union[LLMObsExperimentSpanMeta, UnsetType] = unset,
        metrics: Union[Dict[str, float], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        parent_id: Union[str, UnsetType] = unset,
        span_id: Union[str, UnsetType] = unset,
        start_ns: Union[int, UnsetType] = unset,
        status: Union[LLMObsExperimentSpanStatus, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        trace_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An experiment span enriched with its associated evaluation metrics.

        :param dataset_record_id: ID of the dataset record this span evaluated.
        :type dataset_record_id: str, none_type, optional

        :param duration: Duration of the span in nanoseconds.
        :type duration: float, optional

        :param eval_metrics: Evaluation metrics associated with this span.
        :type eval_metrics: [LLMObsExperimentEvalMetricEvent], optional

        :param id: Unique identifier of the span.
        :type id: str, optional

        :param meta: Metadata associated with an experiment span.
        :type meta: LLMObsExperimentSpanMeta, optional

        :param metrics: Numeric metrics attached to the span.
        :type metrics: {str: (float,)}, optional

        :param name: Name of the span.
        :type name: str, optional

        :param parent_id: Parent span ID, if any.
        :type parent_id: str, optional

        :param span_id: Span ID.
        :type span_id: str, optional

        :param start_ns: Start time in nanoseconds since Unix epoch.
        :type start_ns: int, optional

        :param status: Status of the span.
        :type status: LLMObsExperimentSpanStatus, optional

        :param tags: Tags associated with the span.
        :type tags: [str], optional

        :param trace_id: Trace ID.
        :type trace_id: str, optional
        """
        if dataset_record_id is not unset:
            kwargs["dataset_record_id"] = dataset_record_id
        if duration is not unset:
            kwargs["duration"] = duration
        if eval_metrics is not unset:
            kwargs["eval_metrics"] = eval_metrics
        if id is not unset:
            kwargs["id"] = id
        if meta is not unset:
            kwargs["meta"] = meta
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if name is not unset:
            kwargs["name"] = name
        if parent_id is not unset:
            kwargs["parent_id"] = parent_id
        if span_id is not unset:
            kwargs["span_id"] = span_id
        if start_ns is not unset:
            kwargs["start_ns"] = start_ns
        if status is not unset:
            kwargs["status"] = status
        if tags is not unset:
            kwargs["tags"] = tags
        if trace_id is not unset:
            kwargs["trace_id"] = trace_id
        super().__init__(kwargs)
