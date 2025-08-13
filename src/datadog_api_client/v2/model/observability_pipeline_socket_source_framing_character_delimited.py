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
    from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_character_delimited_method import (
        ObservabilityPipelineSocketSourceFramingCharacterDelimitedMethod,
    )


class ObservabilityPipelineSocketSourceFramingCharacterDelimited(ModelNormal):
    validations = {
        "delimiter": {
            "max_length": 1,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.observability_pipeline_socket_source_framing_character_delimited_method import (
            ObservabilityPipelineSocketSourceFramingCharacterDelimitedMethod,
        )

        return {
            "delimiter": (str,),
            "method": (ObservabilityPipelineSocketSourceFramingCharacterDelimitedMethod,),
        }

    attribute_map = {
        "delimiter": "delimiter",
        "method": "method",
    }

    def __init__(
        self_, delimiter: str, method: ObservabilityPipelineSocketSourceFramingCharacterDelimitedMethod, **kwargs
    ):
        """
        Byte frames which are delimited by a chosen character.

        :param delimiter: A single ASCII character used to delimit events.
        :type delimiter: str

        :param method: Byte frames which are delimited by a chosen character.
        :type method: ObservabilityPipelineSocketSourceFramingCharacterDelimitedMethod
        """
        super().__init__(kwargs)

        self_.delimiter = delimiter
        self_.method = method
