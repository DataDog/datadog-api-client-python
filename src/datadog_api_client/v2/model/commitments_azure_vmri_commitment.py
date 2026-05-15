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
    from datadog_api_client.v2.model.commitments_azure_vmri_status import CommitmentsAzureVMRIStatus


class CommitmentsAzureVMRICommitment(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.commitments_azure_vmri_status import CommitmentsAzureVMRIStatus

        return {
            "benefit_name": (str,),
            "commitment_id": (str,),
            "expiration_date": (str,),
            "instance_type": (str,),
            "meter_sub_category": (str,),
            "region": (str,),
            "start_date": (str,),
            "status": (CommitmentsAzureVMRIStatus,),
            "term_length": (float,),
            "utilization": (float,),
        }

    attribute_map = {
        "benefit_name": "benefit_name",
        "commitment_id": "commitment_id",
        "expiration_date": "expiration_date",
        "instance_type": "instance_type",
        "meter_sub_category": "meter_sub_category",
        "region": "region",
        "start_date": "start_date",
        "status": "status",
        "term_length": "term_length",
        "utilization": "utilization",
    }

    def __init__(
        self_,
        benefit_name: str,
        commitment_id: str,
        instance_type: str,
        meter_sub_category: str,
        region: str,
        status: CommitmentsAzureVMRIStatus,
        expiration_date: Union[str, UnsetType] = unset,
        start_date: Union[str, UnsetType] = unset,
        term_length: Union[float, UnsetType] = unset,
        utilization: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Azure Virtual Machine Reserved Instance commitment details.

        :param benefit_name: The display name of the Azure reservation.
        :type benefit_name: str

        :param commitment_id: The unique identifier of the Reserved Instance.
        :type commitment_id: str

        :param expiration_date: The expiration date of the commitment.
        :type expiration_date: str, optional

        :param instance_type: The Azure VM instance type.
        :type instance_type: str

        :param meter_sub_category: The Azure meter sub-category for the reservation.
        :type meter_sub_category: str

        :param region: The Azure region of the Reserved Instance.
        :type region: str

        :param start_date: The start date of the commitment.
        :type start_date: str, optional

        :param status: Status of an Azure VM Reserved Instance.
        :type status: CommitmentsAzureVMRIStatus

        :param term_length: The term length in years.
        :type term_length: float, optional

        :param utilization: The utilization percentage of the commitment.
        :type utilization: float, optional
        """
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        if start_date is not unset:
            kwargs["start_date"] = start_date
        if term_length is not unset:
            kwargs["term_length"] = term_length
        if utilization is not unset:
            kwargs["utilization"] = utilization
        super().__init__(kwargs)

        self_.benefit_name = benefit_name
        self_.commitment_id = commitment_id
        self_.instance_type = instance_type
        self_.meter_sub_category = meter_sub_category
        self_.region = region
        self_.status = status
