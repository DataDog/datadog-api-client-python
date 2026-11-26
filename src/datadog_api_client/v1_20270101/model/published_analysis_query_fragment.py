# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.published_analysis_query_fragment_data_source import (
        PublishedAnalysisQueryFragmentDataSource,
    )


class PublishedAnalysisQueryFragment(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.published_analysis_query_fragment_data_source import (
            PublishedAnalysisQueryFragmentDataSource,
        )

        return {
            "alias": (str,),
            "data_source": (PublishedAnalysisQueryFragmentDataSource,),
            "dataset_id": (str,),
            "filter": (str,),
            "name": (str,),
        }

    attribute_map = {
        "alias": "alias",
        "data_source": "data_source",
        "dataset_id": "dataset_id",
        "filter": "filter",
        "name": "name",
    }

    def __init__(
        self_,
        data_source: PublishedAnalysisQueryFragmentDataSource,
        dataset_id: str,
        name: str,
        alias: Union[str, UnsetType] = unset,
        filter: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param alias: Test-only generated schema for the dashboard versioning proof of concept.
        :type alias: str, optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: PublishedAnalysisQueryFragmentDataSource

        :param dataset_id: Test-only generated schema for the dashboard versioning proof of concept.
        :type dataset_id: str

        :param filter: Test-only generated schema for the dashboard versioning proof of concept.
        :type filter: str, optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        if alias is not unset:
            kwargs["alias"] = alias
        if filter is not unset:
            kwargs["filter"] = filter
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.dataset_id = dataset_id
        self_.name = name
