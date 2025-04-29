# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_encoding_type import (
        ObservabilityPipelineEnrichmentTableFileEncodingType,
    )


class ObservabilityPipelineEnrichmentTableFileEncoding(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_enrichment_table_file_encoding_type import (
            ObservabilityPipelineEnrichmentTableFileEncodingType,
        )

        return {
            "delimiter": (str,),
            "includes_headers": (bool,),
            "type": (ObservabilityPipelineEnrichmentTableFileEncodingType,),
        }

    attribute_map = {
        "delimiter": "delimiter",
        "includes_headers": "includes_headers",
        "type": "type",
    }

    def __init__(
        self_,
        delimiter: str,
        includes_headers: bool,
        type: ObservabilityPipelineEnrichmentTableFileEncodingType,
        **kwargs,
    ):
        """
        File encoding format.

        :param delimiter: The ``encoding`` ``delimiter``.
        :type delimiter: str

        :param includes_headers: The ``encoding`` ``includes_headers``.
        :type includes_headers: bool

        :param type: Specifies the encoding format (e.g., CSV) used for enrichment tables.
        :type type: ObservabilityPipelineEnrichmentTableFileEncodingType
        """
        super().__init__(kwargs)

        self_.delimiter = delimiter
        self_.includes_headers = includes_headers
        self_.type = type
