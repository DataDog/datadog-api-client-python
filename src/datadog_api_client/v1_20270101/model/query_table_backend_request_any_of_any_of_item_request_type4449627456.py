# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "local_dataset". Must be one of ["local_dataset"].
    :type value: str
    """

    allowed_values = {
        "local_dataset",
    }
    LOCAL_DATASET: ClassVar["QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456.LOCAL_DATASET = (
    QueryTableBackendRequestAnyOfAnyOfItemRequestType4449627456("local_dataset")
)
