# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class EntityContextRevisionsMode(ModelSimple):
    """
    Which revisions to return for each entity: `latest` returns only the latest revision of each entity as of `to`,
        and `all` returns every revision in the requested time range.

    :param value: If omitted defaults to "latest". Must be one of ["latest", "all"].
    :type value: str
    """

    allowed_values = {
        "latest",
        "all",
    }
    LATEST: ClassVar["EntityContextRevisionsMode"]
    ALL: ClassVar["EntityContextRevisionsMode"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


EntityContextRevisionsMode.LATEST = EntityContextRevisionsMode("latest")
EntityContextRevisionsMode.ALL = EntityContextRevisionsMode("all")
