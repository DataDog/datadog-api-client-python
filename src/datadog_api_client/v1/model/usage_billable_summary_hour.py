# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class UsageBillableSummaryHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.usage_billable_summary_keys import UsageBillableSummaryKeys

        return {
            "billing_plan": (str,),
            "end_date": (datetime,),
            "num_orgs": (int,),
            "org_name": (str,),
            "public_id": (str,),
            "ratio_in_month": (float,),
            "start_date": (datetime,),
            "usage": (UsageBillableSummaryKeys,),
        }

    attribute_map = {
        "billing_plan": "billing_plan",
        "end_date": "end_date",
        "num_orgs": "num_orgs",
        "org_name": "org_name",
        "public_id": "public_id",
        "ratio_in_month": "ratio_in_month",
        "start_date": "start_date",
        "usage": "usage",
    }

    def __init__(self, *args, **kwargs):
        """
        Response with monthly summary of data billed by Datadog.

        :param billing_plan: The billing plan.
        :type billing_plan: str, optional

        :param end_date: Shows the last date of usage.
        :type end_date: datetime, optional

        :param num_orgs: The number of organizations.
        :type num_orgs: int, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional

        :param ratio_in_month: Shows usage aggregation for a billing period.
        :type ratio_in_month: float, optional

        :param start_date: Shows the first date of usage.
        :type start_date: datetime, optional

        :param usage: Response with aggregated usage types.
        :type usage: UsageBillableSummaryKeys, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageBillableSummaryHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
