# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineElasticsearchDestinationApiVersion(ModelSimple):
    """
    The Elasticsearch API version to use. Set to `auto` to auto-detect.

    :param value: Must be one of ["auto", "v6", "v7", "v8"].
    :type value: str
    """

    allowed_values = {
        "auto",
        "v6",
        "v7",
        "v8",
    }
    AUTO: ClassVar["ObservabilityPipelineElasticsearchDestinationApiVersion"]
    V6: ClassVar["ObservabilityPipelineElasticsearchDestinationApiVersion"]
    V7: ClassVar["ObservabilityPipelineElasticsearchDestinationApiVersion"]
    V8: ClassVar["ObservabilityPipelineElasticsearchDestinationApiVersion"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineElasticsearchDestinationApiVersion.AUTO = ObservabilityPipelineElasticsearchDestinationApiVersion(
    "auto"
)
ObservabilityPipelineElasticsearchDestinationApiVersion.V6 = ObservabilityPipelineElasticsearchDestinationApiVersion(
    "v6"
)
ObservabilityPipelineElasticsearchDestinationApiVersion.V7 = ObservabilityPipelineElasticsearchDestinationApiVersion(
    "v7"
)
ObservabilityPipelineElasticsearchDestinationApiVersion.V8 = ObservabilityPipelineElasticsearchDestinationApiVersion(
    "v8"
)
