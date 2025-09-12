# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DatastorePrimaryKeyGenerationStrategy(ModelSimple):
    """
    Can be set to `uuid` to automatically generate primary keys when new items are added. Default value is `none`, which requires you to supply a primary key for each new item.

    :param value: Must be one of ["none", "uuid"].
    :type value: str
    """

    allowed_values = {
        "none",
        "uuid",
    }
    NONE: ClassVar["DatastorePrimaryKeyGenerationStrategy"]
    UUID: ClassVar["DatastorePrimaryKeyGenerationStrategy"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DatastorePrimaryKeyGenerationStrategy.NONE = DatastorePrimaryKeyGenerationStrategy("none")
DatastorePrimaryKeyGenerationStrategy.UUID = DatastorePrimaryKeyGenerationStrategy("uuid")
