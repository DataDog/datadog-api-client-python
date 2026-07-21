# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class DdsqlTabularQueryFetchRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "query_id": (str,),
        }

    attribute_map = {
        "query_id": "query_id",
    }

    def __init__(self_, query_id: str, **kwargs):
        """
        Attributes describing which previously submitted DDSQL query to fetch.

        :param query_id: Opaque token returned by an earlier execute or fetch response that carried
            ``state: running``. Identifies the query to poll for results.
        :type query_id: str
        """
        super().__init__(kwargs)

        self_.query_id = query_id
