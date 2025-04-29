# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ObservabilityPipelineAmazonDataFirehoseSourceType(ModelSimple):
    """
    The source type. The value should always be `amazon_data_firehose`.

    :param value: If omitted defaults to "amazon_data_firehose". Must be one of ["amazon_data_firehose"].
    :type value: str
    """

    allowed_values = {
        "amazon_data_firehose",
    }
    AMAZON_DATA_FIREHOSE: ClassVar["ObservabilityPipelineAmazonDataFirehoseSourceType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ObservabilityPipelineAmazonDataFirehoseSourceType.AMAZON_DATA_FIREHOSE = (
    ObservabilityPipelineAmazonDataFirehoseSourceType("amazon_data_firehose")
)
