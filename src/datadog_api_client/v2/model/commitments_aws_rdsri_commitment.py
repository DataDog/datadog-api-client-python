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


class CommitmentsAwsRDSRICommitment(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "commitment_id": (str,),
            "database_engine": (str,),
            "expiration_date": (str,),
            "instance_type": (str,),
            "is_multi_az": (bool,),
            "number_of_nfus": (float,),
            "number_of_reservations": (float,),
            "purchase_option": (str,),
            "region": (str,),
            "start_date": (str,),
            "term_length": (float,),
            "utilization": (float,),
        }

    attribute_map = {
        "commitment_id": "commitment_id",
        "database_engine": "database_engine",
        "expiration_date": "expiration_date",
        "instance_type": "instance_type",
        "is_multi_az": "is_multi_az",
        "number_of_nfus": "number_of_nfus",
        "number_of_reservations": "number_of_reservations",
        "purchase_option": "purchase_option",
        "region": "region",
        "start_date": "start_date",
        "term_length": "term_length",
        "utilization": "utilization",
    }

    def __init__(
        self_,
        commitment_id: str,
        database_engine: str,
        instance_type: str,
        purchase_option: str,
        region: str,
        expiration_date: Union[str, UnsetType] = unset,
        is_multi_az: Union[bool, UnsetType] = unset,
        number_of_nfus: Union[float, UnsetType] = unset,
        number_of_reservations: Union[float, UnsetType] = unset,
        start_date: Union[str, UnsetType] = unset,
        term_length: Union[float, UnsetType] = unset,
        utilization: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS RDS Reserved Instance commitment details.

        :param commitment_id: The unique identifier of the Reserved Instance.
        :type commitment_id: str

        :param database_engine: The database engine of the Reserved Instance.
        :type database_engine: str

        :param expiration_date: The expiration date of the commitment.
        :type expiration_date: str, optional

        :param instance_type: The RDS instance type.
        :type instance_type: str

        :param is_multi_az: Whether the Reserved Instance is Multi-AZ.
        :type is_multi_az: bool, optional

        :param number_of_nfus: The number of Normalized Capacity Units.
        :type number_of_nfus: float, optional

        :param number_of_reservations: The number of reserved instances.
        :type number_of_reservations: float, optional

        :param purchase_option: The payment option for the Reserved Instance.
        :type purchase_option: str

        :param region: The AWS region of the Reserved Instance.
        :type region: str

        :param start_date: The start date of the commitment.
        :type start_date: str, optional

        :param term_length: The term length in years.
        :type term_length: float, optional

        :param utilization: The utilization percentage of the commitment.
        :type utilization: float, optional
        """
        if expiration_date is not unset:
            kwargs["expiration_date"] = expiration_date
        if is_multi_az is not unset:
            kwargs["is_multi_az"] = is_multi_az
        if number_of_nfus is not unset:
            kwargs["number_of_nfus"] = number_of_nfus
        if number_of_reservations is not unset:
            kwargs["number_of_reservations"] = number_of_reservations
        if start_date is not unset:
            kwargs["start_date"] = start_date
        if term_length is not unset:
            kwargs["term_length"] = term_length
        if utilization is not unset:
            kwargs["utilization"] = utilization
        super().__init__(kwargs)

        self_.commitment_id = commitment_id
        self_.database_engine = database_engine
        self_.instance_type = instance_type
        self_.purchase_option = purchase_option
        self_.region = region
