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


class CommitmentsAwsSPCommitment(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "commitment_id": (str,),
            "committed_spend_per_hour": (float,),
            "expiration_date": (str,),
            "purchase_option": (str,),
            "savings_plan_type": (str,),
            "start_date": (str,),
            "term_length": (float,),
            "utilization": (float,),
        }

    attribute_map = {
        "commitment_id": "commitment_id",
        "committed_spend_per_hour": "committed_spend_per_hour",
        "expiration_date": "expiration_date",
        "purchase_option": "purchase_option",
        "savings_plan_type": "savings_plan_type",
        "start_date": "start_date",
        "term_length": "term_length",
        "utilization": "utilization",
    }

    def __init__(
        self_,
        commitment_id: str,
        purchase_option: str,
        savings_plan_type: str,
        committed_spend_per_hour: Union[float, UnsetType] = unset,
        expiration_date: Union[str, UnsetType] = unset,
        start_date: Union[str, UnsetType] = unset,
        term_length: Union[float, UnsetType] = unset,
        utilization: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Savings Plan commitment details.

        :param commitment_id: The unique identifier of the Savings Plan.
        :type commitment_id: str

        :param committed_spend_per_hour: The hourly committed spend for the Savings Plan.
        :type committed_spend_per_hour: float, optional

        :param expiration_date: The expiration date of the commitment.
        :type expiration_date: str, optional

        :param purchase_option: The payment option for the Savings Plan.
        :type purchase_option: str

        :param savings_plan_type: The Savings Plan type.
        :type savings_plan_type: str

        :param start_date: The start date of the commitment.
        :type start_date: str, optional

        :param term_length: The term length in years.
        :type term_length: float, optional

        :param utilization: The utilization percentage of the commitment.
        :type utilization: float, optional
        """
        if committed_spend_per_hour is not unset:
            kwargs["committed_spend_per_hour"] = committed_spend_per_hour
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        if start_date is not unset:
            kwargs["start_date"] = start_date
        if term_length is not unset:
            kwargs["term_length"] = term_length
        if utilization is not unset:
            kwargs["utilization"] = utilization
        super().__init__(kwargs)

        self_.commitment_id = commitment_id
        self_.purchase_option = purchase_option
        self_.savings_plan_type = savings_plan_type
