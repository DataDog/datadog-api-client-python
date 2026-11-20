# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request import ScatterplotBackendTableRequest
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of import (
        ScatterplotBackendTableRequest20270101OneOf,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461521920 import (
        ScatterplotBackendTableRequest20270101OneOf4461521920,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461523200 import (
        ScatterplotBackendTableRequest20270101OneOf4461523200,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461524480 import (
        ScatterplotBackendTableRequest20270101OneOf4461524480,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461525600 import (
        ScatterplotBackendTableRequest20270101OneOf4461525600,
    )
    from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request20270101_one_of4461756480 import (
        ScatterplotBackendTableRequest20270101OneOf4461756480,
    )


class ScatterplotRequests20270101OneOf4461761120(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.scatterplot_backend_table_request import (
            ScatterplotBackendTableRequest,
        )

        return {
            "table": (ScatterplotBackendTableRequest,),
        }

    attribute_map = {
        "table": "table",
    }

    def __init__(
        self_,
        table: Union[
            ScatterplotBackendTableRequest,
            ScatterplotBackendTableRequest20270101OneOf,
            ScatterplotBackendTableRequest20270101OneOf4461521920,
            ScatterplotBackendTableRequest20270101OneOf4461523200,
            ScatterplotBackendTableRequest20270101OneOf4461524480,
            ScatterplotBackendTableRequest20270101OneOf4461525600,
            ScatterplotBackendTableRequest20270101OneOf4461756480,
        ],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param table: Test-only generated schema for the dashboard versioning proof of concept.
        :type table: ScatterplotBackendTableRequest
        """
        super().__init__(kwargs)

        self_.table = table
