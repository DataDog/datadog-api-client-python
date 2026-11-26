# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1_20270101.model.formula_user_journey_query_compute import FormulaUserJourneyQueryCompute
    from datadog_api_client.v1_20270101.model.formula_user_journey_query_data_source import (
        FormulaUserJourneyQueryDataSource,
    )
    from datadog_api_client.v1_20270101.model.user_journey_group_by import UserJourneyGroupBy
    from datadog_api_client.v1_20270101.model.formula_user_journey_query20270101_search import (
        FormulaUserJourneyQuery20270101Search,
    )
    from datadog_api_client.v1_20270101.model.storage_type import StorageType
    from datadog_api_client.v1_20270101.model.legacy_user_journey_search import LegacyUserJourneySearch
    from datadog_api_client.v1_20270101.model.user_journey_search import UserJourneySearch


class FormulaUserJourneyQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.formula_user_journey_query_compute import (
            FormulaUserJourneyQueryCompute,
        )
        from datadog_api_client.v1_20270101.model.formula_user_journey_query_data_source import (
            FormulaUserJourneyQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.user_journey_group_by import UserJourneyGroupBy
        from datadog_api_client.v1_20270101.model.formula_user_journey_query20270101_search import (
            FormulaUserJourneyQuery20270101Search,
        )
        from datadog_api_client.v1_20270101.model.storage_type import StorageType

        return {
            "compute": (FormulaUserJourneyQueryCompute,),
            "data_source": (FormulaUserJourneyQueryDataSource,),
            "exclude_anonymous_traffic": (bool,),
            "group_by": ([UserJourneyGroupBy],),
            "name": (str,),
            "search": (FormulaUserJourneyQuery20270101Search,),
            "storage": (StorageType,),
        }

    attribute_map = {
        "compute": "compute",
        "data_source": "data_source",
        "exclude_anonymous_traffic": "exclude_anonymous_traffic",
        "group_by": "group_by",
        "name": "name",
        "search": "search",
        "storage": "storage",
    }

    def __init__(
        self_,
        compute: FormulaUserJourneyQueryCompute,
        data_source: FormulaUserJourneyQueryDataSource,
        name: str,
        search: Union[FormulaUserJourneyQuery20270101Search, LegacyUserJourneySearch, UserJourneySearch],
        exclude_anonymous_traffic: Union[bool, UnsetType] = unset,
        group_by: Union[List[UserJourneyGroupBy], UnsetType] = unset,
        storage: Union[StorageType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param compute: Test-only generated schema for the dashboard versioning proof of concept.
        :type compute: FormulaUserJourneyQueryCompute

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: FormulaUserJourneyQueryDataSource

        :param exclude_anonymous_traffic: Test-only generated schema for the dashboard versioning proof of concept.
        :type exclude_anonymous_traffic: bool, optional

        :param group_by: Test-only generated schema for the dashboard versioning proof of concept.
        :type group_by: [UserJourneyGroupBy], optional

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param search: Test-only generated schema for the dashboard versioning proof of concept.
        :type search: FormulaUserJourneyQuery20270101Search

        :param storage: Test-only generated schema for the dashboard versioning proof of concept.
        :type storage: StorageType, optional
        """
        if exclude_anonymous_traffic is not unset:
            kwargs["exclude_anonymous_traffic"] = exclude_anonymous_traffic
        if group_by is not unset:
            kwargs["group_by"] = group_by
        if storage is not unset:
            kwargs["storage"] = storage
        super().__init__(kwargs)

        self_.compute = compute
        self_.data_source = data_source
        self_.name = name
        self_.search = search
