# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TreemapBackendRequestAnyOfAnyOfItemRequestType4453530208(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "local_dataset". Must be one of ["local_dataset"].
    :type value: str
    """

    allowed_values = {
        "local_dataset",
    }
    LOCAL_DATASET: ClassVar["TreemapBackendRequestAnyOfAnyOfItemRequestType4453530208"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TreemapBackendRequestAnyOfAnyOfItemRequestType4453530208.LOCAL_DATASET = (
    TreemapBackendRequestAnyOfAnyOfItemRequestType4453530208("local_dataset")
)
