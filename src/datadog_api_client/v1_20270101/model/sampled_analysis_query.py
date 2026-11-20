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
    from datadog_api_client.v1_20270101.model.sampled_analysis_query_sample import SampledAnalysisQuerySample
    from datadog_api_client.v1_20270101.model.sampled_analysis_query_type import SampledAnalysisQueryType


class SampledAnalysisQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.sampled_analysis_query_sample import SampledAnalysisQuerySample
        from datadog_api_client.v1_20270101.model.sampled_analysis_query_type import SampledAnalysisQueryType

        return {
            "query_filter": (str,),
            "sample": (SampledAnalysisQuerySample,),
            "source_dataset": (str,),
            "type": (SampledAnalysisQueryType,),
        }

    attribute_map = {
        "query_filter": "query_filter",
        "sample": "sample",
        "source_dataset": "source_dataset",
        "type": "type",
    }

    def __init__(
        self_,
        sample: SampledAnalysisQuerySample,
        source_dataset: str,
        type: SampledAnalysisQueryType,
        query_filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param query_filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_filter: str, optional

        :param sample: Test-only generated schema for the dashboard versioning proof of concept.
        :type sample: SampledAnalysisQuerySample

        :param source_dataset: Test-only generated schema for the dashboard versioning proof of concept.
        :type source_dataset: str

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: SampledAnalysisQueryType
        """
        if query_filter is not unset:
            kwargs["query_filter"] = query_filter
        super().__init__(kwargs)

        self_.sample = sample
        self_.source_dataset = source_dataset
        self_.type = type
