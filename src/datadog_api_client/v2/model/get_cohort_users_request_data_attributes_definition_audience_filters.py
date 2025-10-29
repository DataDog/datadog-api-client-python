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
    from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_accounts_items import (
        GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersAccountsItems,
    )
    from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_segments_items import (
        GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersSegmentsItems,
    )
    from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_users_items import (
        GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersUsersItems,
    )


class GetCohortUsersRequestDataAttributesDefinitionAudienceFilters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_accounts_items import (
            GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersAccountsItems,
        )
        from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_segments_items import (
            GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersSegmentsItems,
        )
        from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_users_items import (
            GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersUsersItems,
        )

        return {
            "accounts": ([GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersAccountsItems],),
            "formula": (str,),
            "segments": ([GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersSegmentsItems],),
            "users": ([GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersUsersItems],),
        }

    attribute_map = {
        "accounts": "accounts",
        "formula": "formula",
        "segments": "segments",
        "users": "users",
    }

    def __init__(
        self_,
        accounts: Union[
            List[GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersAccountsItems], UnsetType
        ] = unset,
        formula: Union[str, UnsetType] = unset,
        segments: Union[
            List[GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersSegmentsItems], UnsetType
        ] = unset,
        users: Union[List[GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersUsersItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param accounts:
        :type accounts: [GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersAccountsItems], optional

        :param formula:
        :type formula: str, optional

        :param segments:
        :type segments: [GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersSegmentsItems], optional

        :param users:
        :type users: [GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersUsersItems], optional
        """
        if accounts is not unset:
            kwargs["accounts"] = accounts
        if formula is not unset:
            kwargs["formula"] = formula
        if segments is not unset:
            kwargs["segments"] = segments
        if users is not unset:
            kwargs["users"] = users
        super().__init__(kwargs)
