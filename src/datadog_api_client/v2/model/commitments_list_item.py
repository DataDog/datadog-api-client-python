# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class CommitmentsListItem(ModelComposed):
    def __init__(self, **kwargs):
        """
        A commitment item, which varies based on the provider, product, and commitment type.

        :param availability_zone: The availability zone of the reservation.
        :type availability_zone: str, optional

        :param commitment_id: The unique identifier of the Reserved Instance.
        :type commitment_id: str

        :param expiration_date: The expiration date of the commitment.
        :type expiration_date: str, optional

        :param instance_type: The EC2 instance type.
        :type instance_type: str

        :param number_of_nfus: The number of Normalized Capacity Units.
        :type number_of_nfus: float, optional

        :param number_of_reservations: The number of reserved instances.
        :type number_of_reservations: float, optional

        :param offering_class: The offering class of the Reserved Instance.
        :type offering_class: str

        :param operating_system: The operating system of the Reserved Instance.
        :type operating_system: str

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

        :param database_engine: The database engine of the Reserved Instance.
        :type database_engine: str

        :param is_multi_az: Whether the Reserved Instance is Multi-AZ.
        :type is_multi_az: bool, optional

        :param cache_engine: The cache engine type of the Reserved Instance.
        :type cache_engine: str

        :param committed_spend_per_hour: The hourly committed spend for the Savings Plan.
        :type committed_spend_per_hour: float, optional

        :param savings_plan_type: The Savings Plan type.
        :type savings_plan_type: str

        :param benefit_name: The display name of the Azure reservation.
        :type benefit_name: str

        :param meter_sub_category: The Azure meter sub-category for the reservation.
        :type meter_sub_category: str

        :param status: Status of an Azure VM Reserved Instance.
        :type status: CommitmentsAzureVMRIStatus
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
        from datadog_api_client.v2.model.commitments_aws_ec2_ri_commitment import CommitmentsAwsEC2RICommitment
        from datadog_api_client.v2.model.commitments_aws_rdsri_commitment import CommitmentsAwsRDSRICommitment
        from datadog_api_client.v2.model.commitments_aws_elasticache_ri_commitment import (
            CommitmentsAwsElasticacheRICommitment,
        )
        from datadog_api_client.v2.model.commitments_aws_sp_commitment import CommitmentsAwsSPCommitment
        from datadog_api_client.v2.model.commitments_azure_vmri_commitment import CommitmentsAzureVMRICommitment
        from datadog_api_client.v2.model.commitments_azure_compute_sp_commitment import (
            CommitmentsAzureComputeSPCommitment,
        )

        return {
            "oneOf": [
                CommitmentsAwsEC2RICommitment,
                CommitmentsAwsRDSRICommitment,
                CommitmentsAwsElasticacheRICommitment,
                CommitmentsAwsSPCommitment,
                CommitmentsAzureVMRICommitment,
                CommitmentsAzureComputeSPCommitment,
            ],
        }
