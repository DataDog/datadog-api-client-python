# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateAppsDatastoreResponseDataType(ModelSimple):
    """
    Datastores resource type.

    :param value: If omitted defaults to "datastores". Must be one of ["datastores"].
    :type value: str
    """

    allowed_values = {
        "datastores",
    }
    DATASTORES: ClassVar["CreateAppsDatastoreResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateAppsDatastoreResponseDataType.DATASTORES = CreateAppsDatastoreResponseDataType("datastores")
