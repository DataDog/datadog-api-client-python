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
    from datadog_api_client.v1_20270101.model.apm_issue_stream_query_data_source import APMIssueStreamQueryDataSource
    from datadog_api_client.v1_20270101.model.apm_issue_stream_query_investigation import (
        APMIssueStreamQueryInvestigation,
    )
    from datadog_api_client.v1_20270101.model.issue_stream_persona import IssueStreamPersona
    from datadog_api_client.v1_20270101.model.issue_stream_sort import IssueStreamSort
    from datadog_api_client.v1_20270101.model.issue_stream_state import IssueStreamState


class APMIssueStreamQuery(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1_20270101.model.apm_issue_stream_query_data_source import (
            APMIssueStreamQueryDataSource,
        )
        from datadog_api_client.v1_20270101.model.apm_issue_stream_query_investigation import (
            APMIssueStreamQueryInvestigation,
        )
        from datadog_api_client.v1_20270101.model.issue_stream_persona import IssueStreamPersona
        from datadog_api_client.v1_20270101.model.issue_stream_sort import IssueStreamSort
        from datadog_api_client.v1_20270101.model.issue_stream_state import IssueStreamState

        return {
            "assignee_uuids": ([str],),
            "code_gen_fix_states": ([str],),
            "cross_org_uuids": ([str],),
            "data_source": (APMIssueStreamQueryDataSource,),
            "indexes": ([str],),
            "investigation": (APMIssueStreamQueryInvestigation,),
            "muted": (bool,),
            "persona": (IssueStreamPersona,),
            "query_string": (str,),
            "sort": (IssueStreamSort,),
            "states": ([IssueStreamState],),
            "suspected_causes": ([str],),
            "team_handles": ([str],),
        }

    attribute_map = {
        "assignee_uuids": "assignee_uuids",
        "code_gen_fix_states": "code_gen_fix_states",
        "cross_org_uuids": "cross_org_uuids",
        "data_source": "data_source",
        "indexes": "indexes",
        "investigation": "investigation",
        "muted": "muted",
        "persona": "persona",
        "query_string": "query_string",
        "sort": "sort",
        "states": "states",
        "suspected_causes": "suspected_causes",
        "team_handles": "team_handles",
    }

    def __init__(
        self_,
        data_source: APMIssueStreamQueryDataSource,
        query_string: str,
        assignee_uuids: Union[List[str], UnsetType] = unset,
        code_gen_fix_states: Union[List[str], UnsetType] = unset,
        cross_org_uuids: Union[List[str], UnsetType] = unset,
        indexes: Union[List[str], UnsetType] = unset,
        investigation: Union[APMIssueStreamQueryInvestigation, UnsetType] = unset,
        muted: Union[bool, UnsetType] = unset,
        persona: Union[IssueStreamPersona, UnsetType] = unset,
        sort: Union[IssueStreamSort, UnsetType] = unset,
        states: Union[List[IssueStreamState], UnsetType] = unset,
        suspected_causes: Union[List[str], UnsetType] = unset,
        team_handles: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param assignee_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type assignee_uuids: [str], optional

        :param code_gen_fix_states: Test-only generated schema for the dashboard versioning proof of concept.
        :type code_gen_fix_states: [str], optional

        :param cross_org_uuids: Test-only generated schema for the dashboard versioning proof of concept.
        :type cross_org_uuids: [str], optional

        :param data_source: Test-only generated schema for the dashboard versioning proof of concept.
        :type data_source: APMIssueStreamQueryDataSource

        :param indexes: Test-only generated schema for the dashboard versioning proof of concept.
        :type indexes: [str], optional

        :param investigation: Test-only generated schema for the dashboard versioning proof of concept.
        :type investigation: APMIssueStreamQueryInvestigation, optional

        :param muted: Test-only generated schema for the dashboard versioning proof of concept.
        :type muted: bool, optional

        :param persona: Test-only generated schema for the dashboard versioning proof of concept.
        :type persona: IssueStreamPersona, optional

        :param query_string: Test-only generated schema for the dashboard versioning proof of concept.
        :type query_string: str

        :param sort: Test-only generated schema for the dashboard versioning proof of concept.
        :type sort: IssueStreamSort, optional

        :param states: Test-only generated schema for the dashboard versioning proof of concept.
        :type states: [IssueStreamState], optional

        :param suspected_causes: Test-only generated schema for the dashboard versioning proof of concept.
        :type suspected_causes: [str], optional

        :param team_handles: Test-only generated schema for the dashboard versioning proof of concept.
        :type team_handles: [str], optional
        """
        if assignee_uuids is not unset:
            kwargs["assignee_uuids"] = assignee_uuids
        if code_gen_fix_states is not unset:
            kwargs["code_gen_fix_states"] = code_gen_fix_states
        if cross_org_uuids is not unset:
            kwargs["cross_org_uuids"] = cross_org_uuids
        if indexes is not unset:
            kwargs["indexes"] = indexes
        if investigation is not unset:
            kwargs["investigation"] = investigation
        if muted is not unset:
            kwargs["muted"] = muted
        if persona is not unset:
            kwargs["persona"] = persona
        if sort is not unset:
            kwargs["sort"] = sort
        if states is not unset:
            kwargs["states"] = states
        if suspected_causes is not unset:
            kwargs["suspected_causes"] = suspected_causes
        if team_handles is not unset:
            kwargs["team_handles"] = team_handles
        super().__init__(kwargs)

        self_.data_source = data_source
        self_.query_string = query_string
