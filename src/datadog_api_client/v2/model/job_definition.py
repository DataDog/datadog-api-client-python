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
    from datadog_api_client.v2.model.calculated_field import CalculatedField
    from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
    from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
    from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
    from datadog_api_client.v2.model.security_monitoring_standard_rule_query import SecurityMonitoringStandardRuleQuery
    from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
    from datadog_api_client.v2.model.security_monitoring_third_party_rule_case_create import (
        SecurityMonitoringThirdPartyRuleCaseCreate,
    )


class JobDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.calculated_field import CalculatedField
        from datadog_api_client.v2.model.security_monitoring_rule_case_create import SecurityMonitoringRuleCaseCreate
        from datadog_api_client.v2.model.security_monitoring_filter import SecurityMonitoringFilter
        from datadog_api_client.v2.model.security_monitoring_rule_options import SecurityMonitoringRuleOptions
        from datadog_api_client.v2.model.security_monitoring_standard_rule_query import (
            SecurityMonitoringStandardRuleQuery,
        )
        from datadog_api_client.v2.model.security_monitoring_reference_table import SecurityMonitoringReferenceTable
        from datadog_api_client.v2.model.security_monitoring_third_party_rule_case_create import (
            SecurityMonitoringThirdPartyRuleCaseCreate,
        )

        return {
            "calculated_fields": ([CalculatedField],),
            "cases": ([SecurityMonitoringRuleCaseCreate],),
            "filters": ([SecurityMonitoringFilter],),
            "_from": (int,),
            "index": (str,),
            "message": (str,),
            "name": (str,),
            "options": (SecurityMonitoringRuleOptions,),
            "queries": ([SecurityMonitoringStandardRuleQuery],),
            "reference_tables": ([SecurityMonitoringReferenceTable],),
            "tags": ([str],),
            "third_party_cases": ([SecurityMonitoringThirdPartyRuleCaseCreate],),
            "to": (int,),
            "type": (str,),
        }

    attribute_map = {
        "calculated_fields": "calculatedFields",
        "cases": "cases",
        "filters": "filters",
        "_from": "from",
        "index": "index",
        "message": "message",
        "name": "name",
        "options": "options",
        "queries": "queries",
        "reference_tables": "referenceTables",
        "tags": "tags",
        "third_party_cases": "thirdPartyCases",
        "to": "to",
        "type": "type",
    }

    def __init__(
        self_,
        cases: List[SecurityMonitoringRuleCaseCreate],
        _from: int,
        index: str,
        message: str,
        name: str,
        queries: List[SecurityMonitoringStandardRuleQuery],
        to: int,
        calculated_fields: Union[List[CalculatedField], UnsetType] = unset,
        filters: Union[List[SecurityMonitoringFilter], UnsetType] = unset,
        options: Union[SecurityMonitoringRuleOptions, UnsetType] = unset,
        reference_tables: Union[List[SecurityMonitoringReferenceTable], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        third_party_cases: Union[List[SecurityMonitoringThirdPartyRuleCaseCreate], UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Definition of a historical job.

        :param calculated_fields: Calculated fields.
        :type calculated_fields: [CalculatedField], optional

        :param cases: Cases used for generating job results.
        :type cases: [SecurityMonitoringRuleCaseCreate]

        :param filters: Additional queries to filter matched events before they are processed. This field is deprecated for log detection, signal correlation, and workload security rules.
        :type filters: [SecurityMonitoringFilter], optional

        :param _from: Starting time of data analyzed by the job.
        :type _from: int

        :param index: Index used to load the data.
        :type index: str

        :param message: Message for generated results.
        :type message: str

        :param name: Job name.
        :type name: str

        :param options: Options on rules.
        :type options: SecurityMonitoringRuleOptions, optional

        :param queries: Queries for selecting logs analyzed by the job.
        :type queries: [SecurityMonitoringStandardRuleQuery]

        :param reference_tables: Reference tables for the rule.
        :type reference_tables: [SecurityMonitoringReferenceTable], optional

        :param tags: Tags for generated signals.
        :type tags: [str], optional

        :param third_party_cases: Cases for generating results from third-party rules. Only available for third-party rules.
        :type third_party_cases: [SecurityMonitoringThirdPartyRuleCaseCreate], optional

        :param to: Ending time of data analyzed by the job.
        :type to: int

        :param type: Job type.
        :type type: str, optional
        """
        if calculated_fields is not unset:
            kwargs["calculated_fields"] = calculated_fields
        if filters is not unset:
            kwargs["filters"] = filters
        if options is not unset:
            kwargs["options"] = options
        if reference_tables is not unset:
            kwargs["reference_tables"] = reference_tables
        if tags is not unset:
            kwargs["tags"] = tags
        if third_party_cases is not unset:
            kwargs["third_party_cases"] = third_party_cases
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.cases = cases
        self_._from = _from
        self_.index = index
        self_.message = message
        self_.name = name
        self_.queries = queries
        self_.to = to
