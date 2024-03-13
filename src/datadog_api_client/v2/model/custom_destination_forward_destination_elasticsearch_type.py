# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CustomDestinationForwardDestinationElasticsearchType(ModelSimple):
    """
    Type of the Elasticsearch destination.

    :param value: If omitted defaults to "elasticsearch". Must be one of ["elasticsearch"].
    :type value: str
    """

    allowed_values = {
        "elasticsearch",
    }
    ELASTICSEARCH: ClassVar["CustomDestinationForwardDestinationElasticsearchType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CustomDestinationForwardDestinationElasticsearchType.ELASTICSEARCH = (
    CustomDestinationForwardDestinationElasticsearchType("elasticsearch")
)
