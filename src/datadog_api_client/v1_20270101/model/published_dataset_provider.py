# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PublishedDatasetProvider(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["ddsql_query", "notebook_cell"].
    :type value: str
    """

    allowed_values = {
        "ddsql_query",
        "notebook_cell",
    }
    DDSQL_QUERY: ClassVar["PublishedDatasetProvider"]
    NOTEBOOK_CELL: ClassVar["PublishedDatasetProvider"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PublishedDatasetProvider.DDSQL_QUERY = PublishedDatasetProvider("ddsql_query")
PublishedDatasetProvider.NOTEBOOK_CELL = PublishedDatasetProvider("notebook_cell")
