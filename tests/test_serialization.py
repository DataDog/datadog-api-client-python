from datadog_api_client.model_utils import (
    datetime,
    UUID
)
from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
from datadog_api_client.v2.model.logs_group_by import LogsGroupBy
from datadog_api_client.v2.model.logs_group_by_missing import LogsGroupByMissing
from datadog_api_client.v2.model.logs_group_by_total import LogsGroupByTotal
from datadog_api_client.v2.model.logs_aggregate_sort import LogsAggregateSort
from datadog_api_client.v2.model.logs_aggregate_sort_type import LogsAggregateSortType
from datadog_api_client.v2.model.logs_aggregation_function import LogsAggregationFunction
from datadog_api_client.v2.model.logs_sort_order import LogsSortOrder
from datadog_api_client.v2.model.user_invitation_data_attributes import UserInvitationDataAttributes


def test_default_coerce():
    thresholds = MonitorThresholds(critical=5)
    assert thresholds["critical"] == 5.0


def test_primitive_one_of():
    group_by = LogsGroupBy(
        facet="host",
        missing=LogsGroupByMissing("miss"),
        sort=LogsAggregateSort(
            type=LogsAggregateSortType("measure"),
            order=LogsSortOrder("asc"),
            aggregation=LogsAggregationFunction("pc90"),
            metric="@duration",
        ),
        total=LogsGroupByTotal("recall"),
    )

    assert group_by.missing == "miss"

def test_uuid_model():
    user_invitation_data_attributes = UserInvitationDataAttributes(
        created_at = datetime.fromisoformat("2022-05-12T09:53:38.990217+00:00"),
        expires_at= datetime.fromisoformat("2022-05-14T09:53:38.846030+00:00"),
        invite_type= "openid_invite",
        uuid = "65ef03ae-d1d9-11ec-ad3d-da7ad0900002"
    )
    assert isinstance(user_invitation_data_attributes.uuid,UUID)
