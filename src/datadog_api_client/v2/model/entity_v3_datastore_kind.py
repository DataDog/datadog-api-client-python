# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityV3DatastoreKind(ModelSimple):
    """
    The definition of Entity V3 Datastore Kind object.

    :param value: If omitted defaults to "datastore". Must be one of ["datastore"].
    :type value: str
    """

    allowed_values = {
        "datastore",
    }
    DATASTORE: ClassVar["EntityV3DatastoreKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityV3DatastoreKind.DATASTORE = EntityV3DatastoreKind("datastore")
