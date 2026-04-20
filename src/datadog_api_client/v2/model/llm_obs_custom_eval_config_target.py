# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_custom_eval_config_eval_scope import LLMObsCustomEvalConfigEvalScope


class LLMObsCustomEvalConfigTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_custom_eval_config_eval_scope import LLMObsCustomEvalConfigEvalScope

        return {
            "application_name": (str,),
            "enabled": (bool,),
            "eval_scope": (LLMObsCustomEvalConfigEvalScope,),
            "filter": (str, none_type),
            "root_spans_only": (bool, none_type),
            "sampling_percentage": (float, none_type),
        }

    attribute_map = {
        "application_name": "application_name",
        "enabled": "enabled",
        "eval_scope": "eval_scope",
        "filter": "filter",
        "root_spans_only": "root_spans_only",
        "sampling_percentage": "sampling_percentage",
    }

    def __init__(
        self_,
        application_name: str,
        enabled: bool,
        eval_scope: Union[LLMObsCustomEvalConfigEvalScope, UnsetType] = unset,
        filter: Union[str, none_type, UnsetType] = unset,
        root_spans_only: Union[bool, none_type, UnsetType] = unset,
        sampling_percentage: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Target application configuration for a custom evaluator.

        :param application_name: Name of the ML application this evaluator targets.
        :type application_name: str

        :param enabled: Whether the evaluator is active for the target application.
        :type enabled: bool

        :param eval_scope: Scope at which to evaluate spans.
        :type eval_scope: LLMObsCustomEvalConfigEvalScope, optional

        :param filter: Filter expression to select which spans to evaluate.
        :type filter: str, none_type, optional

        :param root_spans_only: When true, only root spans are evaluated.
        :type root_spans_only: bool, none_type, optional

        :param sampling_percentage: Percentage of traces to evaluate. Must be greater than 0 and at most 100.
        :type sampling_percentage: float, none_type, optional
        """
        if eval_scope is not unset:
            kwargs["eval_scope"] = eval_scope
        if filter is not unset:
            kwargs["filter"] = filter
        if root_spans_only is not unset:
            kwargs["root_spans_only"] = root_spans_only
        if sampling_percentage is not unset:
            kwargs["sampling_percentage"] = sampling_percentage
        super().__init__(kwargs)

        self_.application_name = application_name
        self_.enabled = enabled
