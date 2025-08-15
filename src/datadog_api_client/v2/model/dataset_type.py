# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatasetType(ModelSimple):
    """
    Resource type, always set to `dataset`.

    :param value: If omitted defaults to "dataset". Must be one of ["dataset"].
    :type value: str
    """

    allowed_values = {
        "dataset",
    }
    DATASET: ClassVar["DatasetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatasetType.DATASET = DatasetType("dataset")
