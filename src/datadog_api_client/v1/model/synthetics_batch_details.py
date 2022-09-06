# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SyntheticsBatchDetails(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_batch_details_data import SyntheticsBatchDetailsData

        return {
            "data": (SyntheticsBatchDetailsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, *args, **kwargs):
        """
        Details about a batch response.

        :param data: Wrapper object that contains the details of a batch.
        :type data: SyntheticsBatchDetailsData, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
