# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class UsageCIVisibilityHour(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "ci_pipeline_indexed_spans": (int,),
            "ci_test_indexed_spans": (int,),
            "ci_visibility_pipeline_committers": (int,),
            "ci_visibility_test_committers": (int,),
            "org_name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "ci_pipeline_indexed_spans": "ci_pipeline_indexed_spans",
        "ci_test_indexed_spans": "ci_test_indexed_spans",
        "ci_visibility_pipeline_committers": "ci_visibility_pipeline_committers",
        "ci_visibility_test_committers": "ci_visibility_test_committers",
        "org_name": "org_name",
        "public_id": "public_id",
    }

    def __init__(self, *args, **kwargs):
        """
        CI visibility usage in a given hour.

        :param ci_pipeline_indexed_spans: The number of spans for pipelines in the queried hour.
        :type ci_pipeline_indexed_spans: int, optional

        :param ci_test_indexed_spans: The number of spans for tests in the queried hour.
        :type ci_test_indexed_spans: int, optional

        :param ci_visibility_pipeline_committers: Shows the total count of all active Git committers for Pipelines in the current month. A committer is active if they commit at least 3 times in a given month.
        :type ci_visibility_pipeline_committers: int, optional

        :param ci_visibility_test_committers: The total count of all active Git committers for tests in the current month. A committer is active if they commit at least 3 times in a given month.
        :type ci_visibility_test_committers: int, optional

        :param org_name: The organization name.
        :type org_name: str, optional

        :param public_id: The organization public ID.
        :type public_id: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(UsageCIVisibilityHour, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
