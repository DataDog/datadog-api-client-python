# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class LegacyIssueStreamRequest20270101Query(ModelComposed):
    def __init__(self, **kwargs):
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
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v1.model.apm_issue_stream_query import APMIssueStreamQuery
        from datadog_api_client.v1.model.rum_issue_stream_query import RUMIssueStreamQuery
        from datadog_api_client.v1.model.logs_issue_stream_query import LogsIssueStreamQuery

        return {
            "oneOf": [
                APMIssueStreamQuery,
                RUMIssueStreamQuery,
                LogsIssueStreamQuery,
            ],
        }
