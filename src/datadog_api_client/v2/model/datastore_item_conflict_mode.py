# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatastoreItemConflictMode(ModelSimple):
    """
    How to handle conflicts when inserting items that already exist in the datastore.

    :param value: Must be one of ["fail_on_conflict", "overwrite_on_conflict"].
    :type value: str
    """

    allowed_values = {
        "fail_on_conflict",
        "overwrite_on_conflict",
    }
    FAIL_ON_CONFLICT: ClassVar["DatastoreItemConflictMode"]
    OVERWRITE_ON_CONFLICT: ClassVar["DatastoreItemConflictMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatastoreItemConflictMode.FAIL_ON_CONFLICT = DatastoreItemConflictMode("fail_on_conflict")
DatastoreItemConflictMode.OVERWRITE_ON_CONFLICT = DatastoreItemConflictMode("overwrite_on_conflict")
