const tool = load("tool.js");
(function logic() {
  function init_refund_table_data(
    product_id,
    full_sku_code,
    start_date,
    end_date,
    supply
  ) {
    var table = new tool.table("订单表-原始表");
    table.init_table([
      "子订单编号",
      "商品单价",
      "商品数量",
      "结算金额",
      "订单应付金额",
      "平台服务费",
      "商品ID",
      "订单阶段",
      "结算阶段",
      "供应商",
      "订单提交日期",
      "结算日期",
      "几天发货",
      "几天退款",
      "几天结算",
    ]);

    var headers = ["渠道", "订单数", "付款数"];
    for (var i = 0; i < 20; i++) {
      headers.push(`${i}天`);
    }
    var index = ["退货率", "总退货率", "退货数"];
    var dash_board_refund = new tool.dashboard_tool(table, headers, index);
    var filter = dash_board_refund.init_order_filter(
      product_id,
      full_sku_code,
      start_date,
      end_date,
      supply
    );

    let query_set = {
      useFieldName: true,
      groupByFieldList: table.get_field_list(["几天退货", "订单阶段"]),
      aggregationQueryList: [
        {
          field: table.get_field("子订单编号"),
          func: "count",
          distinct: false,
        },
        { field: table.get_field("商品数量"), func: "sum", distinct: false },
      ],
    };

    if (filter.conditionList.length > 0) {
      query_set.filter = filter;
    }
    var resp = table.query(query_set);
    var data = resp.list;
    var c = collect(data);
    return "test";
  }
  return {
    init_refund_table_data: init_refund_table_data,
  };
})();
