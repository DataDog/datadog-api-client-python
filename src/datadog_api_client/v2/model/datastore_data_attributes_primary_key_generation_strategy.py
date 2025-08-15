# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatastoreDataAttributesPrimaryKeyGenerationStrategy(ModelSimple):
    """
    The `attributes` `primary_key_generation_strategy`.

    :param value: Must be one of ["none", "uuid"].
    :type value: str
    """

    allowed_values = {
        "none",
        "uuid",
    }
    NONE: ClassVar["DatastoreDataAttributesPrimaryKeyGenerationStrategy"]
    UUID: ClassVar["DatastoreDataAttributesPrimaryKeyGenerationStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatastoreDataAttributesPrimaryKeyGenerationStrategy.NONE = DatastoreDataAttributesPrimaryKeyGenerationStrategy("none")
DatastoreDataAttributesPrimaryKeyGenerationStrategy.UUID = DatastoreDataAttributesPrimaryKeyGenerationStrategy("uuid")
