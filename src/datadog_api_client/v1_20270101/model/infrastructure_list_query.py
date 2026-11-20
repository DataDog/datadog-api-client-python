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
    from datadog_api_client.v1_20270101.model.infrastructure_list_query_data_source import (
        InfrastructureListQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.container_view import ContainerView


class InfrastructureListQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.infrastructure_list_query_data_source import (
            InfrastructureListQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.container_view import ContainerView

        return {
            "data_source": (InfrastructureListQueryDataSource,),
            "query_string": (str,),
            "resource_type": (ContainerView,),
        }

    attribute_map = {
        "data_source": "data_source",
        "query_string": "query_string",
        "resource_type": "resource_type",
    }

    def __init__(
        self_,
        data_source: InfrastructureListQueryDataSource,
        query_string: str,
        resource_type: Union[ContainerView, str],
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: InfrastructureListQueryDataSource

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param resource_type: Test-only generated schema for the dashboard versioning proof of concept.
        :type resource_type: ContainerView
        """
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
        self_.resource_type = resource_type
