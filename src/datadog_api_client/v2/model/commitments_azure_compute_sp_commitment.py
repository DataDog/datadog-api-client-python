# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class CommitmentsAzureComputeSPCommitment(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "benefit_name": (str,),
            "commitment_id": (str,),
            "committed_spend_per_hour": (float,),
            "expiration_date": (str,),
            "savings_plan_type": (str,),
            "start_date": (str,),
            "term_length_months": (int,),
            "utilization": (float,),
        }

    attribute_map = {
        "benefit_name": "benefit_name",
        "commitment_id": "commitment_id",
        "committed_spend_per_hour": "committed_spend_per_hour",
        "expiration_date": "expiration_date",
        "savings_plan_type": "savings_plan_type",
        "start_date": "start_date",
        "term_length_months": "term_length_months",
        "utilization": "utilization",
    }

    def __init__(
        self_,
        benefit_name: str,
        commitment_id: str,
        committed_spend_per_hour: Union[float, UnsetType] = unset,
        expiration_date: Union[str, UnsetType] = unset,
        savings_plan_type: Union[str, UnsetType] = unset,
        start_date: Union[str, UnsetType] = unset,
        term_length_months: Union[int, UnsetType] = unset,
        utilization: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Azure Compute Savings Plan commitment details.

        :param benefit_name: The display name of the Azure Savings Plan.
        :type benefit_name: str

        :param commitment_id: The unique identifier of the Savings Plan.
        :type commitment_id: str

        :param committed_spend_per_hour: The hourly committed spend for the Savings Plan.
        :type committed_spend_per_hour: float, optional

        :param expiration_date: The expiration date of the commitment.
        :type expiration_date: str, optional

        :param savings_plan_type: The Azure Savings Plan type, ``Compute`` or ``Database`` , based on the product order name. Omitted when
            the type can't be classified.
        :type savings_plan_type: str, optional

        :param start_date: The start date of the commitment.
        :type start_date: str, optional

        :param term_length_months: The commitment term in whole months. Omitted when the term is unknown.
        :type term_length_months: int, optional

        :param utilization: The utilization percentage of the commitment, from 0 to 100.
        :type utilization: float, optional
        """
        if committed_spend_per_hour is not unset:
            kwargs["committed_spend_per_hour"] = committed_spend_per_hour
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        if savings_plan_type is not unset:
            kwargs["savings_plan_type"] = savings_plan_type
        if start_date is not unset:
            kwargs["start_date"] = start_date
        if term_length_months is not unset:
            kwargs["term_length_months"] = term_length_months
        if utilization is not unset:
            kwargs["utilization"] = utilization
        super().__init__(kwargs)

        self_.benefit_name = benefit_name
        self_.commitment_id = commitment_id
