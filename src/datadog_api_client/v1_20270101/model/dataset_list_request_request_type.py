# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatasetListRequestRequestType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "dataset_list_rows". Must be one of ["dataset_list_rows"].
    :type value: str
    """

    allowed_values = {
        "dataset_list_rows",
    }
    DATASET_LIST_ROWS: ClassVar["DatasetListRequestRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatasetListRequestRequestType.DATASET_LIST_ROWS = DatasetListRequestRequestType("dataset_list_rows")
