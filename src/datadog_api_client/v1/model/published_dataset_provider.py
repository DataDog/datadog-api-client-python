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
    Product page that published the dataset queried by a `DatasetListQuery`. `ddsql_query` is the only provider currently supported for host map widgets.

    :param value: If omitted defaults to "ddsql_query". Must be one of ["ddsql_query"].
    :type value: str
    """

    allowed_values = {
        "ddsql_query",
    }
    DDSQL_QUERY: ClassVar["PublishedDatasetProvider"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PublishedDatasetProvider.DDSQL_QUERY = PublishedDatasetProvider("ddsql_query")
